const mongoose = require('mongoose');

mongoose.Promise=global.Promise;

before(done => {
  mongoose.connect('mongodb://localhost/muber_test',{useMongoClient:true});
  mongoose.connection
  .once('open', () => done())
  .on('error', err => {
    console.warn('Warning',error);
  });
});

beforeEach(done => {
  const { drivers } = mongoose.connection.collections;
  drivers.drop()
    .then(() => done())
    // then promise will be executed if no error
    .catch(() => done());
    // catch promise will be executed if error
    // What error can be occured?
    // ==> When executed first, there is no driver collection
});
