const assert = require('assert')
const User = require('../src/user')

describe('Deleting a user',()=>{
  let joe;

  beforeEach((done)=>{
    joe = new User({name:'Joe'});
    joe.save()
      .then(()=>done());
  });

  it('model instance remove',(done)=>{
    joe.remove()
      .then(() => User.findOne({ name:'Joe'}))
      .then((user) => {
        assert(user === null);
        // {} is empty-object, not null
        done();
      });
      // joe.remove().then().then() -> chained-on function
      // each result will be propagate
      // chained-on function == executing subsequently
  });

  it('class method remove',(done)=>{
    // Remove a bunch of records with some given criteria
    User.remove({ name:'Joe'})
      .then(() => User.findOne({ name:'Joe'}))
      .then((user)=>{
        assert(user === null);
        done();
      });
  });

  it('class method findOneAndRemove',(done)=>{
    // Remove first-searched record with some given criteria
    User.findOneAndRemove({ name:'Joe'})
      .then(() => User.findOne({ name:'Joe'}))
      .then((user)=>{
        assert(user === null);
        done();
      });
  });

  it('class method findByIdAndRemove',(done)=>{
    // No need to put Object, just ID form
    User.findByIdAndRemove(joe._id)
      .then(() => User.findOne({ name:'Joe'}))
      .then((user)=>{
        assert(user === null);
        done();
      });
  });
});
