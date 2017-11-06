function greet(callback){
    console.log('hello !');

    var data={
        name:'John'
    }

    callback(data);
}

greet(function(data){
    console.log('my name is lee !');
    console.log(data);
})

greet(function(data){
    console.log("what's yours?");
    console.log(data.name);
})