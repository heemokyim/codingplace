var http = require('http');
var fs = require('fs');

http.createServer(function(req, res){

    res.writeHead(200,{'Content-Type':'application/json'});
    var obj ={
        first:'John',
        last:'Doe'
    }
    // sending and receiving JSON thru HTTP
    // depart -> serialize -> web -> deserialize -> dest
    res.end(JSON.stringify(obj));

}).listen(1337,'127.0.0.1'); 