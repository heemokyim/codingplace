var http = require('http');
var fs = require('fs');

// how to put different content according to URL?
// == Routing !
http.createServer(function(req, res){
    // req.method() == Determine Get or Post
    // should deal each separately

    if(req.url==='/'){
        // Remember ReadableStream.pipe(WritableStream)
        fs.createReadStream(__dirname+'/index1.html').pipe(res);
    }

    // a == b -> operator try to convert it's type
    // a=== b -> that won't happen
    else if(req.url==='/api'){
    res.writeHead(200,{'Content-Type':'application/json'});
    var obj ={
        first:'John',
        last:'Doe'
    }
    res.end(JSON.stringify(obj));
    }

    // 404 no web-page avaiable
    // 400 doesn't understand what it means
    else{
        res.writeHead(404);
        res.end();
    }
    // what if no else-if?
    // == check every if, not efficient

}).listen(1337,'127.0.0.1'); 