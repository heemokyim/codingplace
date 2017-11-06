// please go get this and bring it for me
// == require()
var greet=require('./requiree.js');

// greet() is in requiree.js,
// then will greet() be executed?
// No ! because it's in another module!
// something in module doesn't effect in other's scope
// if module.exports doesn't happen
greet();