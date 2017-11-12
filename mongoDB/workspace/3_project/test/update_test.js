const assert = require('assert');
const User = require('../src/user');

describe('Updating records', ()=>{
  let joe;

  beforeEach((done)=>{
    joe = new User({ name:'Joe', postCount:0});
    joe.save()
      .then(() => done());
  });

  function assertName(operation, done){
    operation
      // User.find({}) == every data in User collection
      .then(() => User.find({}))
      .then((users) => {
        assert(users.length === 1);
        assert(users[0].name === 'Alex');
        done();
      });
  }

  it('instance type using set and save', (done)=>{
    joe.set('name','Alex');
    assertName(joe.save(), done);
  });

  it('a model instance can update', (done)=>{
    assertName(joe.update({ name:'Alex'}), done)
  });

  it('a model class can update',(done)=>{
    // Update a bunch of records with some given criteria
    assertName(
      User.update({ name:'Joe' }, { name:'Alex'}),
      done
    )
  });

  it('a model class can update one record',(done)=>{
    assertName(
      User.findOneAndUpdate({ name:'Joe'},{ name:'Alex'}),
      done
    )
  });

  it('a model class can find a record with an ID and update',(done)=>{
    assertName(
      User.findByIdAndUpdate(joe._id, { name:'Alex'}),
      done
    )
  });

  it('A user can have their postcount incremented by 1',(done) => {
    // Making lots of update in one go with efficiency?
    // ==> Update Operator
    // https://docs.mongodb.com/manual/reference/operator/update/
    // Using these operators is more performant

    User.update({ name: 'Joe'}, { $inc: { postCount:10}})
    // Update every User instance's postCount + 1
      .then(()=> User.findOne({ name: 'Joe'}))
      .then((user)=>{
        assert(user.postCount === 10);
        done();
      });
  });
});

// ** set and save pattern example
// function nameUpdate(user){}
// function emailUpdate(user){}
// nameUpdate(user);
// emailUpdate(user);
// user.save();
