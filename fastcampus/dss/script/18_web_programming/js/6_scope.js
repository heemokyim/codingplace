// var a = 'hello'
//
// function func(){
//   console.log(a)
// }
//
// func();

// var a= 'hello'
// function func(){
//   var a= 'javascript'
//   console.log('inner',a) // javascript
// }
//
// func();
// console.log('outer',a)  // hello

// var a= 'hello'
// function func(){
//   a = 'javascript'
//   consle.log(a)
// }
// func()
// console.log(a)

(function(){
  var a = 'hello'
  console.log(a)
}());

console.log(a);
