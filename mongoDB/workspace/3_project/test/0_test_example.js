// * mocha == testing library for nodejs

// Note 3_how_mocha_works.PNG
// how mocha actually works?
// 0. "test":"mocha" in package.json->scripts (4_npm_run_test.PNG)
// 1. it inside describe (block or function)
// 2. assertion inside it
// 3. npm run test

// * assert == to define test e.g. i hope this value equlas that value

// this is how mocha-test works
const assert = require('assert');

// Important to explicitly name test-case
describe('Describe test here', ()=>{
  it('for each test', (done)=>{
    assert(1 + 1 === 2);
    done();
    // i hope 1+1 equals 2
    // if it's true, pass otherwise fail
  });
});
