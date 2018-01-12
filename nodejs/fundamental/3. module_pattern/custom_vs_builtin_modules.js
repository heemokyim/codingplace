// custom module = './util.js'
// builtin(core,native) module = 'util'
// like <built_in>, "custom"
var util=require('util');

var name='woong';
var greeting=util.format('hello %s',name);
util.log(greeting)