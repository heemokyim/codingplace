// JS engine will be pickier about code
// not to make any silly mistakes
'use strict';
// a = 3; this expression won't be executed even if it can be

// function just same with function_constructor_example.js
// this is syntatic sugar
class Person{
    constructor(first,last){
        this.first=first;
        this.last=last;
    }

    // setting up prototype-chain
    greet(){
        console.log('hello'+this.first+this.last)
    }
}

// takeaway = class syntax is really powerful
//          = but don't forget what's going under hood

var john=new Person('Woong','Lee')
john.greet()


var jane=new Person('Jane','Parlia')
jane.greet()

console.log(john.__proto__)
console.log(jane.__proto__)
console.log(john.__proto__=== jane.__proto__)