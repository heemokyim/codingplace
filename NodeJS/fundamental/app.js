var express=require('express');
var app=express();

app.set('port',process.env.PORT||3000);

app.get('/',function(req,res){});

app.post('/',function(req,res){});

app.use('/assets',express.statid(__dirname+"/public"));

app.set('view engine','ejs');