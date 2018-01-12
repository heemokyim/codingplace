var express = require('express');
var app = express();
var port = process.env.PORT || 3000;

var api=require('./controller/apiCon');
var html=require('./controller/htmlCon');

app.use('/assets',express.static(__dirname+'/public'));

app.set('view engine','ejs');

app.use('/',function(req,res,next){
    console.log('Requestd Url: '+req.url);
    next();
});

api(app);
html(app);

app.listen(port);