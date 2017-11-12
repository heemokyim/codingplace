// One of additive features Mongoose provides

const assert = require('assert');
const User = require('../src/user');

describe('Validating records', ()=>{
  it('requires a user name', (done)=>{
    const user = new User({ name: undefined})
    // Reason why {name:undefined} instead of {} ?
    // To specify this test is about name for other people

    // all the results of validating user model
    const validationResult = user.validateSync();
    // user.validate((validationResult)=>{ assert })
    // validateSync() VS validate()
    // readFileSync() VS readFile()

    // You can try this to see what's going on in result !
    // Rly depply nested !
    // console.log(validationResult);

    const { message } = validationResult.errors.name;
    // const message = validationResult.errors.name.message;

    assert(message === 'Name is required.');
    done();
  });

  it('requires a user\'s name longer than 2 characters',(done)=>{
    const user = new User( {name:'Al'});
    const validationResult = user.validateSync();
    const { message } = validationResult.errors.name;

    assert(message === 'Name must be longer than 2 characters.');
    done();
  });

  it('disallows invalid records from being saved',(done)=>{
    const user = new User({name: 'Al'});
    user.save()
      // Why catch this time?
      // Because user.save() will fail.
      .catch((validationResult)=>{
        const { message } = validationResult.errors.name;

        assert(message === 'Name must be longer than 2 characters.');
        done();
      });
  });
});
