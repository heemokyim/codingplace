const assert = require('assert');
const User = require('../src/user');

describe('Reading users out of database', ()=>{

  let joe;

  beforeEach((done)=>{
    joe = new User({name:'Joe'});
    joe.save()
      .then(() => done());
  });

  it('finds all users with a name of joe', (done)=>{
    // find all users
    User.find({name:'Joe'})
            // result of User.find
      .then((listOfUsers)=>{
        // console.log(listOfUsers[0]._id);
        // console.log(joe._id);
        // Upper two seem identical but below comparison will fail
        assert(listOfUsers[0]._id.toString() === joe._id.toString());
        // Why?
        // because instance._id is object, not raw string
        done();
      });
  });

  it('finds a user with a particular id', (done)=>{
      // In here, you don't need to toString
      // Mongoose will take care internally
      User.findOne({ _id:joe._id})
        .then((user)=>{
          assert(user.name === 'Joe');
          done();
        });
  });
});
