var express = require('express');
var app = express();
var port = process.env.PORT || 3000;

var mysql=require('mysql');

var api=require('./controller/apiCon');
var html=require('./controller/htmlCon');

app.use('/assets',express.static(__dirname+'/public'));

app.set('view engine','ejs');

app.use('/',function(req,res,next){
    console.log('Requestd Url: '+req.url);

    var con = mysql.createConnection({
        host:'localhost',
        
        user:'test',
        password:'password',
        database:'addressbook'
    });

    // callback after running SQL
    // 1. call tabular data from DB
    // 2. convert it to [JSON,JSON...] == rows
    con.query(SQL,function(err,rows){
        if(err) throw err;
        console.log(rows);
    });

    next();
});

api(app);
html(app);

app.listen(port);

// How DB to Client?
// 1. connect to DB
// 2. call tabular data from DB
// 3. stream.pipe(tabular data)