var http = require('http');
var mongoose = require('mongoose');

http.createServer(function(req, res){
    // status code = 200, Content-Type = text/plain
    res.writeHead(200,{'Content-Type':'text/plain'});
    // res.end = sending only this one
    res.end('Hello world\n');

    console.log(req)



}).listen(1337,'127.0.0.1');
