'use strict';

var Greetr=require('./greetr')
var greetr=new Greetr();

greetr.on('greet',function(data){
    console.log('someone greeted !' + data)
});

greetr.greet('woong')