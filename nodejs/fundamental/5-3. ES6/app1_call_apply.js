var obj={
    name:'John Doe',
    greet:function(){
        console.log(`Hello ${this.name}`);
    }
}

obj.greet();
obj.greet.call({name:'Jane Doe'});
obj.greet.apply({name:'Jane Doe'})

// obj.greet() vs call()
// change this keyword to passed argument

// call() vs apply()
// * Common = change this keyword to passed argument

// * Difference =
// if function has parameters,
// call passes each of them (param1,param2,...)
// apply passes single array including them([param1,param2,...])

