const serverless = require('serverless-http');
const express = require('express')
const app = express()

app.get('/hello', function (req, res) {
  res.send('Hello World!')
})

app.get('/', function (req, res) {
  res.send('Hello World 7!')
})

module.exports.handler = serverless(app);