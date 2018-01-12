// below is function constructor !
function Person(first,last){
    this.first=first
    this.last=last
}

// refer 'greet' to prototype of Person
// prototype.greet() <- Perseon
Person.prototype.greet=function(){
    console.log('my name is '+this.first+this.last);
};

var john=new Person('Woong','Lee')

console.log(john['first'])

// By prototypal inheritance, (using binary tree?) only leaves are properties
// john can use directly greet from its prototype
// prototype chain searches john !
john.greet()


var jane=new Person('Jane','Parlia')
jane.greet()

// how to check prototype?
console.log(john.__proto__)
console.log(jane.__proto__)
console.log(john.__proto__=== jane.__proto__)