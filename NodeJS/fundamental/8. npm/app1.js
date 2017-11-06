var http = require('http');
var fs = require('fs');

// Use nodemon to run
// nodemon app1.js in cmd
// nodemon supports CLI so it can be executed in cmd

http.createServer(function(req, res){
    if(req.url==='/'){
        fs.createReadStream(__dirname+'/index1.html').pipe(res);
    }

    else if(req.url==='/api'){
    res.writeHead(200,{'Content-Type':'application/json'});
    var obj ={
        first:'John',
        last:'gilly'
    };
    res.end(JSON.stringify(obj));
    }

    else{
        res.writeHead(404);
        res.end();
    }
}).listen(1337,'127.0.0.1');
