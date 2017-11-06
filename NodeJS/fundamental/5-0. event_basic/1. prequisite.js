// object props and methods
var obj={
    greet:'Hello'
};

console.log(obj.greet);
console.log(obj['greet']);

var prop='greet';
console.log(obj[prop]);

// functions and arrays
var arr=[];

arr.push(function(){
    console.log('hello world 1')
});
arr.push(function(){
    console.log('hello world 2')
});
arr.push(function(){
    console.log('hello world 3')
});

// equal to ' for each in arr ' in python
// item = each, elems of arr
arr.forEach(function(item){
    item();
});

for(i=0;i<arr.length;i++){
    arr[i]();
}