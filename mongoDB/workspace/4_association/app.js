const User = require('./src/user');
const mongoose=require('mongoose');

mongoose.Promise=global.Promise;

mongoose.connect('mongodb://localhost/users_test',{useMongoClient:true});

mongoose.connection
  .once('open',()=>{ console.log('MongoDB Connected !') })
  .on('error',(error)=>{
    console.warn('Warning !',error);
  });

// let joe = new User({name:'Joe'});

// joe.save();

// console.log('saved')

// console.log(mongoose.connection.collections)
