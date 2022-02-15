var express = require("express");
var app = express();
var port = 3700;
 
// app.get("/", function(req, res){
//     res.send("It works!");
// });

app.use(express.static(__dirname + '/public'));

//app.listen(port);
var io = require('socket.io').listen(app.listen(port));

console.log("Listening on port " + port);


io.sockets.on('connection', function (socket) {
	//console.log("connection established ");
    socket.emit('message', { message: 'welcome to the chat' });
    socket.on('send', function (data) {
        io.sockets.emit('message', data);
    });
});
//alert('gdysgyds');
app.set('views', __dirname + '/tpl');
app.set('view engine', "jade");
app.engine('jade', require('jade').__express);
app.get("/", function(req, res){
    res.render("page");
});