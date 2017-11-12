const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const UserSchema = new Schema({
  name: {
    type: String,
    validate:{
      // validator: (name)=>name.length>2 ,
      validator: (name) => {
        if(name.length>2){
          return true
        }
        else{
          return false
        }
      },
      // if validator == False
      message: 'Name must be longer than 2 characters.'
    },
    required: [true, 'Name is required.']
  },
  postCount: Number
});

const User = mongoose.model('user', UserSchema);
// 1. if not 'user' in DB, make 'user' collection
// 2. 'user' collection follows UserSchema
// User == entire collection
// will be stord as 'users' in MongoDB

module.exports=User;
