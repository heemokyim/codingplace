const assert=require('assert');
const User=require('../src/user')
// why capitalize head of name? (User)
// specify this is special, like Class

describe('Creating records',()=>{
  it('saves a user', (done)=>{
    const joe = new User({ name:'Joe' });
    // joe becomes instance of User collection

    joe.save()
      .then(()=>{
        // Has joe been saved successfully?
        assert(!joe.isNew);
        done();
        // Pause other test(s) until this completed !
        // done can be accessed thru every it, beforeEach
      });
    // save instance to MongoDB
  });
});
