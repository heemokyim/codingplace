var express=require('express');
var app=express();

var bodyParser=require('body-parser');

var urlencodedParser = bodyParser.urlencoded({ extended: false });
var jsonParser = bodyParser.json();

app.set('port',process.env.PORT || 3000);
app.listen(app.get('port'),function(){
    console.log(app.get('port'));
});

app.set('view engine','ejs');

app.get('/api/person/:id',function(req,res){
    // get that info with :id
});

app.post('/api/person/changeSomething',jsonParser,function(req,res){
    // chagne info in DB
});

app.delete('/api/person/changeSomething',function(req,res){
    // delete something in DB
});

// REST? = just follows good URL structure