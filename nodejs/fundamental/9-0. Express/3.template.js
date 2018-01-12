// npm install ejs --save

var express = require('express');
var app = express();

var port = process.env.PORT || 3000;

app.use('/assets',express.static(__dirname+'/public'));

// param1 = view engine , param2 = template engine
// View engine searchs View files in folder 'views'
// Yes. that View from MVC Pattern
app.set('view engine','ejs');

app.use('/',function(req,res,next){
    console.log('Requestd Url: '+req.url);
    next();
});

app.get('/',function(req,res){
    // According to app.set, it searches *.ejs
    // param1 = View
    res.render('index');
});

app.get('/person/:id',function(req,res){
    var id=req.params.id;

    // param1 = View, param2 = Model
    // pass {ID:id} to view/person.ejs
    var obj={
        IDqwe:id,
        length:id.length
    };
    res.render('person',obj)
});

app.get('/api',function(req,res){
    res.json({first:'John',last:'Doe'});
});

app.listen(port);