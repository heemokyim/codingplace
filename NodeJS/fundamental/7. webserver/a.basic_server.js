var http = require('http');

// argument is callback function
// callback() by V8 after http.createServer() by OS

// whenever req happens,
// below is executed with req, res 
http.createServer(function(req, res){
    // status code = 200, Content-Type = text/plain
    res.writeHead(200,{'Content-Type':'text/plain'});
    // res.end = sending only this one
    res.end('Hello world\n');

    // Port number, IP Address
}).listen(1337,'127.0.0.1');

// 1. res is writable stream
// 2. F12 when debugging in chrome browser