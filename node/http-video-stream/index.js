const fs = require("fs");
const requestIp = require('request-ip');
const ip6addr = require('ip6addr');
const express = require("express");
const app = express();

// inside middleware handler
const ipMiddleware = function(req, res, next) {
    const clientIp = requestIp.getClientIp(req);
    //console.log('clientIp', clientIp)
    let addr = ip6addr.parse(clientIp)
    //console.log('addr', addr)
    //console.log(addr.toString({ format: 'auto' }))
    //console.log('clientIp: ', ip6addr.parse(clientIp).toString({'format': 'v4'}))
    next();
};

app.get("/link", function (req, res) {
  res.sendFile(__dirname + "/index.html");
});

app.get("/video", ipMiddleware, function (req, res) {

    //const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
    //console.log(ip); // ip address of the user

    // Ensure there is a range given for the video
    const range = req.headers.range;
    if (!range) {
      res.status(400).send("Requires Range header");
    }
  
    // get video stats (about 105MB)
    const videoPath = "video1.mp4";
    const videoSize = fs.statSync("video1.mp4").size;
  
    // Parse Range
    // Example: "bytes=32324-"
    const CHUNK_SIZE = 10 ** 6; // 1MB
    const start = Number(range.replace(/\D/g, ""));
    const end = Math.min(start + CHUNK_SIZE, videoSize - 1);
  
    // Create headers
    const contentLength = end - start + 1;
    const headers = {
      "Content-Range": `bytes ${start}-${end}/${videoSize}`,
      "Accept-Ranges": "bytes",
      "Content-Length": contentLength,
      "Content-Type": "video/mp4",
    };
  
    // HTTP Status 206 for Partial Content
    res.writeHead(206, headers);
    //console.log(start, end, CHUNK_SIZE);
    // create video read stream for this particular chunk
    const videoStream = fs.createReadStream(videoPath, { start, end });
  
    // Stream the video chunk to the client
    videoStream.pipe(res);
});

app.listen(3000, function () {
  console.log("Listening on port 3000!");
});