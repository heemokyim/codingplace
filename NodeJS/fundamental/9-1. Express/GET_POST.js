var express = require('express');
var app = express();
var port = process.env.PORT || 3000;

// npm install body-parser -- save
// To process POST
var bodyParser=require('body-parser');
// For req.body
var urlencodedParser = bodyParser.urlencoded({ extended: false });
// For req.body of JSON
var jsonParser = bodyParser.json();

app.use('/assets',express.static(__dirname+'/public'));

app.set('view engine','ejs');

app.use('/',function(req,res,next){
    console.log('Requestd Url: '+req.url);
    next();
});

app.get('/',function(req,res){
    res.render('index');
});

// Query is within URL from http request
// == req.query
app.get('/person/:id',function(req,res){
    var obj={
        ID:req.params.id,

        // Use req.query to deal with info from GET
        QSTR:req.query.qstr
    };

    res.render('person',obj)
});

// Query is within body of http request
// == req.body (reason why bodyParser)

// POST /person to process String
// urlencodedParser(){middleware} -> last callback()
app.post('/person/',urlencodedParser, function(req,res){
    res.send('Thank you !');

    // req.body is added because of urlencodedParser
    console.log(req.body.first);
    console.log(req.body.last);
});

// Post /personjson to process json data
// jsonParser(){middleware} -> last callback()
app.post('/personjson',jsonParser,function(req,res){
    res.send('Thank you for json data !');

    console.log(req.body.first);
    console.log(req.body.last);
});

app.get('/api',function(req,res){
    res.json({first:'John',last:'Doe'});
});

app.listen(port);