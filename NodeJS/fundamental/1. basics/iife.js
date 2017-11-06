var first='jane';

//IIFE = Immediately invoked function expression
(function(last){
    // this 'first' is scoped inside of this function
    // no confusion with upper one

    var first='john';
    console.log(first+last)
}('Doe'))
// immediately invoke function after statement 
// (parenthesis after statement)

console.log(first)