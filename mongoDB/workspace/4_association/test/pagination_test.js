const assert = require('assert');
const User = require('../src/user');

describe('Pagination : Skip and Limit', ()=>{

  let joe, maria, alex, zach;

  beforeEach((done)=>{
    joe = new User({name:'Joe'});
    maria = new User({name:'Maria'});
    alex = new User({name:'Alex'});
    zach = new User({name:'Zach'});

    // Why Promise.all?
    // To keep in order for test
    Promise.all([joe.save(),maria.save(),alex.save(),zach.save()])
      .then(()=>done());
  });

  it('can skip and limit the result set', (done)=>{
    // User.find({}) ? == there is no FILTER
    // which means bring all records
    User.find({})
      .sort({ name: 1})
      // sort({ criteria : 1 or -1 })
      // 1 ascending, -1 descending
      .skip(1)
      .limit(2)
      .then((users)=>{
        assert(users.length == 2);
        assert(users[0].name === 'Joe');
        assert(users[1].name === 'Maria');
        done();
      });
  });
});
