// require returns {} because assignment to exports
// not module.exports
var greet=require('./greet')

// To point same spot by using only exports,
// mutate representation using exports
// like exports.greet
// (= module.exports.greet, prototypal inheritance)
var greet2=require('./greet2')
greet2.greet()

// so what's the conclusion?
// just use module.exports 
// because exports==module.exports