const wrStream = require('stream').Writable;
const util = require('util');

// stream.Writable == abstract class
// so that we need to implement .write()
function customWrite(){
    wrStream.call(this);
    this._write=function(chunk,encoding,callback){
        // Do what is supposed to do here.
        console.log(chunk.toString());
        if (callback!=null){
            callback();
        }
    }
}
util.inherits(customWrite,wrStream);

module.exports=customWrite;