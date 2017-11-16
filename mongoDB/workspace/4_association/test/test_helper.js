const mongoose=require('mongoose');

mongoose.Promise=global.Promise;

before((done)=>{
  mongoose.connect('mongodb://localhost/users_test',{useMongoClient:true});

  mongoose.connection
    .once('open',()=>{ done(); })
    .on('error',(error)=>{
      console.warn('Warning !',error);
    });
});

beforeEach((done)=>{
  // ES6 code
  const { users, comments, blogposts } = mongoose.connection.collections;

  // There is no operation drop whole collection in Mongoose
  // And below chained-on dropping doesn't look good
  // How can we deal with this?
  // ==> Loop
  users.drop(()=>{
    comments.drop(()=>{
      blogposts.drop(()=>{
        done();
      });
    });
  });
});
