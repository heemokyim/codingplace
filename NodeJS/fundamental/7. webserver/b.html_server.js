// how to put html into response?
// 1. read content from html
// 2. put content into response
// 3. some other template for placeholder

var fs=require('fs');

var http=require('http');

http.createServer(function(req,res){
    // text/plain -> text/html
    // what if  html file with text/plain?
    res.writeHead(200,{'Content-Type':'text/html'});

    //var html  holds the content
    var html=fs.readFileSync(__dirname+'/index.html','utf8');
    var message='Hello World';

    // placeholder is changed to what's in it message
    // {Message}
    html = html.replace('{Message}',message);
    res.end(html);
}).listen(1337,'127.0.0.1');