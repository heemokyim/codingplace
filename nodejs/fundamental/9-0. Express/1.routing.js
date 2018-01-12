var express = require('express');
var app = express();

var port = process.env.PORT || 3000;

app.get('/',function(req,res){
    res.send('<html><head></head><body><h1>Hell12o world!</h1></body></html>')
});

// :id -> req.params.id, :id1 -> req.params.id1
app.get('/person/:id-(:id1)?',function(req,res){
    var a=req.params.id1 || "";
    var b=req.params.id || "";
    res.send('<html><head></head><body><h1>Person: '+a + b+'</h1></body></html>')
});

app.get('/api',function(req,res){
    res.json({first:'John',last:'Doe'});
});

app.listen(port);