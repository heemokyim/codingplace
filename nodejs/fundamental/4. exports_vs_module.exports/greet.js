// unlike assignment toward module.export,
// (exports and module.export point same memory space)
// assignment to variable in JS makes new spot in memory

// but require returns module.export and according to upper,
// require returns {}
exports=function(){
    console.log('hello')
}

console.log(exports)
console.log(module.exports)