var express = require('express');
var app = express();
var port = process.env.PORT || 3000;

var mongoose=require('mongoose');
mongoose.Promise=require('bluebird');

// URL from MongoLab
// 1. Go to mLab.com
// 2. create suitable DB
// 3. go to Users tab
// 4. create DB Users (Never set same ID PWD)
// 5. mongodb://<dbuser>:<dbpassword>@ds125365.mlab.com:25365/nodetodosample
// put thme in place holders <>
mongoose.connect('mongodb://test:test@ds125365.mlab.com:25365/nodetodosample',{
    useMongoClient:true
});

var Schema = mongoose.Schema;

var personSchema = new Schema({
    first:String,
    last:String,
    addr:String
});

// make constrouctor from Schema
var Person=mongoose.model('Person',personSchema);

// create instance
var john=Person({
    first:'lee',
    last:'woong',
    addr:'nowhere'
});

// save the instance to MongoDB
// Won't work if account is read-only
    // instance.save()
    // model.create(array of instance)
john.save(function(err){
    if(err) throw err;
    console.log('Person saved');
})

// after saving it to DB,
// you can check it at DB

var api=require('./controller/apiCon');
var html=require('./controller/htmlCon');

app.use('/assets',express.static(__dirname+'/public'));

app.set('view engine','ejs');

app.use('/',function(req,res,next){
    console.log('Requestd Url: '+req.url);

    // why are JS and MongoDB matched so well?
    // == similar structure inside of it
    // get all users
    // {} means all
    Person.find({},function(err,users){
        if(err) throw err;

        console.log(users);
    });

    next();
});

api(app);
html(app);

app.listen(port);