const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const PostSchema = require('./post');

const UserSchema = new Schema({
  name: {
    type: String,
    // below validate feature is only available with Mongoose
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
    // NOT NULL Integrity
    required: [true, 'Name is required.']
  },
  posts: [PostSchema],
  likes: Number
  // postCount:Number
},{usePushEach:true});

// postCount is derivative from posts
// Don't need to be stored in DB
// fit for virtual type
UserSchema.virtual('postCount').get(function(){
  return this.posts.length;
});

const User = mongoose.model('user', UserSchema);
// 1. if not 'user' in DB, make 'user' collection
// 2. 'user' collection follows UserSchema
// User == entire collection
// will be stord as 'users' in MongoDB

module.exports=User;
