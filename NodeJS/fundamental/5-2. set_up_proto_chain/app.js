var person={
    first:'',
    last:'',
    greet:function(){
        return this.first+' '+this.last;
    }
}

var john=Object.create(person);
john.first="John";
john.last="Doe";

var jane=Object.create(person);
jane.first="Jane";
jane.last="Doe";

console.log(john.greet());
console.log(jane.greet());
