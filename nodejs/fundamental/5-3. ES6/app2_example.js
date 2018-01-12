var util=require('util')

function Person(){
    // 2. Person() is called by call(this), Object(this) from Policeman()
    // Object(this) from Policeman's first, last become 'John','Doe'
    this.first='John';
    this.last='Doe';
}

Person.prototype.greet=function(){
    console.log('Hello '+this.first+this.last)
}

function Policeman(){
    // 1. By doing below, Person() is passed Object from Policeman()
    Person.call(this);
    this.number='1234';
}

util.inherits(Policeman,Person);
var officer=new Policeman();
officer.greet();