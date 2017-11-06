const mongoose=require('mongoose');
// const = i will not change this thru code

mongoose.connect('mongodb://localhost/users_test');
// mongodb://ADDRESS:PORT/NAME_OF_DATABASE_IN_MONGODB
// remote MongoDB => mongodb://43.52.6.1:4000/users_test
// local MongoDB => mongodb://localhost/users_test
//                        no needs to specify port

mongoose.connection
  // open은 pipe.on('data',callback)처럼 reserved된 놈인듯
  .once('open',()=>{console.log('Good to go !')})
  // error도
  .on('error',(error)=>{
    console.warn('Warning !',error);
  });
// (new events()).once(eventName,callback)
// If triggered once, that event will be removed

// fat arrow is =>
