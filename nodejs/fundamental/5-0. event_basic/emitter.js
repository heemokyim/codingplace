function Emitter(){
    this.events={
    };
};

// 1.
// on is custom name
// when applicable events happen, listener will be invoked
// which is function
Emitter.prototype.on = function(type,listener){
    // this.events[type] || [] ?
    // if this.events[type] == None, then empty array
    this.events[type] = this.events[type] || [];
    this.events[type].push(listener);
};

// 2.
// emit is custom name
// after mapping event and listener, (what and how)
// and gotta say 'hey something happened, i'm emmitting event !'
// this is it.
Emitter.prototype.emit = function(type){
    if(this.events[type]) {
                                    // function(param)
                                    // param = elems in array
        this.events[type].forEach(function(listener){
            listener();
        });
    }
};

module.exports=Emitter;

// How can we use event emitter?
// 1. map events and listener               = on
// 2. run proper listener for its event     = emit
// 3. this is called Emitter
// 4. expose Emitter thru module.exports