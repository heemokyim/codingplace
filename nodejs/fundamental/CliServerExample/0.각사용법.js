var express=require('express');
var app=express();

var bodyParser=require('body-parser');

// For req.body
var urlencodedParser = bodyParser.urlencoded({ extended: false });
// For req.body of JSON
var jsonParser = bodyParser.json();

// setting port
app.set('port',process.env.PORT || 3000);
app.listen(app.get('port'),function(){
    console.log(app.get('port'));
});

// setting view engine from MVC
app.set('view engine','ejs');

// middleware between request and response
app.get('/',function(req,res){
    res.render('client');
});

// res.render = passing front-end
app.get('/1',function(req,res){
    res.render('client1');
});

// GET, req.query
app.get('/first',function(req,res){
    req.query.item;
});

// POST, return string
app.post('/second',urlencodedParser,function(req,res){
    req.body.item;
});


// POST, return JSON
app.post('/third',jsonParser,function(req,res){
    req.body.item;
});

// ** How to Respond?
// res.send, res.json, res.render, res.end
// or Stream0.pipe(Stream1)

// ** How to check items in Request?
// req.params.item, req.query.item, req.body.item
// :id -> req.params.id, :id1 -> req.params.id1