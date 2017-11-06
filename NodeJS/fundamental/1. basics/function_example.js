// function statement
function greet(){
    console.log("hi")
}

greet();

//functions are first-class
function logGreeting(fn){
    fn();
};

// functions in JS are object (special kinda)
// and the reason why this is proper is because
// function in JS is first class.
// (every other operation can be applied to function)

// takeaway = function can be used as argument
logGreeting(greet);

// function expression 
var greetMe = function(){
    console.log('Hi Tony');
}

greetMe();

logGreeting(greetMe);

//use a function  expression on the fly
logGreeting(function(){
    console.log('Wow awesome pattern !');
});