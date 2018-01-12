var express = require('express');
var app = express();

var port = process.env.PORT || 3000;

// ** param1 = variable name, param2 = resource path
app.use('/assets',express.static(__dirname+'/public'));
// This is how mapping URL with Directory
// now belows are same dir
// D:\OneDrive\CodingPlace\NodeJS\9-0. Express\public
// /assets

// Middleware
// = something functiong between things (request, response)
// whenever '/' routing hits, this callback is called. (like union operation)
// ex) localhost:3000/ , localhost:3000/api

// app.use(middleware);
app.use('/',function(req,res,next){
    console.log('Requestd Url: '+req.url);
    
    // run the next middleware
    // In this case, next is get
    next();
});

app.get('/',function(req,res){
         // ** Using static files in public as assets
    res.send('<html><head><link href=/assets/style.css type=text/css rel=stylesheet /></head><body><h1>Hello world!</h1></body></html>');
});

app.get('/person/:id-(:id1)?',function(req,res){
    var a=req.params.id1 || "";
    var b=req.params.id || "";
    res.send('<html><head></head><body><h1>Person: '+a + b+'</h1></body></html>')
});

app.get('/api',function(req,res){
    res.json({first:'John',last:'Doe'});
});

// all routings above are MIDDLEWARE
// between Request and Response, do something 

// 1. Check middleware package in Expressjs.com
// 2. npm install
// 3. app.use(require)

// Reason why Express is so popular
// Really easy to use middleware (define things between somethings)

app.listen(port);