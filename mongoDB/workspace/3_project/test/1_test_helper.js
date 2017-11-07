const mongoose=require('mongoose');
// const = i will not change this thru code

mongoose.Promise=global.Promise;
// * Why doing this ?
// == Mongoose's default promise lib is deprecated
// Note 9_mongoose_default_promises_library.PNG
// global.Promise == ES6 Promise library


// before() is also hook
// before() VS beforeEach()
//  once vs   every time before whole test
before((done)=>{
  mongoose.connect('mongodb://localhost/users_test',{useMongoClient:true});
  // mongodb://ADDRESS:PORT/NAME_OF_DATABASE_IN_MONGODB
  // remote MongoDB => mongodb://43.52.6.1:4000/users_test
  // local MongoDB => mongodb://localhost/users_test
  //                in local, no needs to specify port
  // If there is users_test, use it
  // else make users_test database

  mongoose.connection
    // open은 pipe.on('data',callback)처럼 reserved된 놈인듯
    .once('open',()=>{ done(); })
    // error도
    .on('error',(error)=>{
      console.warn('Warning !',error);
    });
  // once?
  // (new events()).once(eventName,callback)
  // If triggered once, that event will be removed

  // fat arrow is =>
});

// * hook = code to execute before test
// beforeEach() is hook
// when to use? removing every from DB before test
// because MongoDB allows duplication
beforeEach((done)=>{
  // 1. take all
  // 2. remove
  mongoose.connection.collections.users.drop(()=>{
    // Ready to run the next test !
    done();
  });
});
// * done = prevent undesired result of test
// because of asynchronous feature from NodeJS
// ex) Before removing, test can be executed
// available to every it and beforeEach block
