// pass by value
function change(b){
    b=2;
}

// doesn't impact on a
var a=1;
change(a);
console.log(a)

function changeObj(d){
    d.prop1=function(){};

    // below {} means object
    d.prop2={}
}

var c={};
changeObj(c)
console.log(c)

// takeaway = primitives are passed by value
//          = objects are passed by reference