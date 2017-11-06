// npm install express --save (on cmd)
var express = require('express');
var app = express();

// To set port in windows powershell,
// $env:PORT = portYouWant
var port = process.env.PORT || 3000;

    // param1 = URL, param2 = what gonna do when param1
app.get('/',function(req,res){
    res.send('<html><head></head><body><h1>Hell12o world!</h1></body></html>')
});

app.get('/api',function(req,res){
    res.json({first:'John',last:'Doe'});
});

//http.createServer().listen(3000);
app.listen(port);

