var fs=require('fs');

var http=require('http');

http.createServer(function(req,res){

    // think about html_server.js in terms of performance
    // 1. request comes in
    // 2. bring full data into memory
    // 3. send them back in response
    // 4. go to 1

    // then what if file is big and so many request?
    // == Steram !

    res.writeHead(200,{'Content-Type':'text/html'});
    // response object is writable stream so that can be piped
    fs.createReadStream(__dirname+'/index1.html').pipe(res);

}).listen(1337,'127.0.0.1');

// how can we check performance?
// F12 in browser and see reponse time