const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const UserSchema = new Schema({
  name: String
});

const User = mongoose.model('user', UserSchema);
// 1. if not 'user' in DB, make 'user' collection
// 2. 'user' collection follows UserSchema
// User == entire collection
// will be stord as 'users' in MongoDB

module.exports=User;
