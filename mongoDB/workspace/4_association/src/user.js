const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const PostSchema = require('./post');

const UserSchema = new Schema({
  name: {
    type: String,
    validate:{
      validator: (name)=>name.length>2 ,
      message: 'Name must be longer than 2 characters.'
    },
    required: [true, 'Name is required.']
  },
  posts: [PostSchema],
  likes: Number,

  blogPosts:[{
    type:Schema.Types.ObjectId,
    ref:'blogPost'
  }]

},{usePushEach:true});

UserSchema.virtual('postCount').get(function(){
  return this.posts.length;
});

// If we remove user, Relavant blogPosts should be removed
// We can do this by Middleware
// Refer to 6_middleware_as_cascade_delete

// This is middleware declaration
// 1. Watch for the 'remove' event
// 2. middleware is defined as callback
UserSchema.pre('remove',function(next){
  const BlogPost = mongoose.model('blogPost');
  // No worry of deadlock (Cyclic Require) if like this

  // Let's think of How we can do this.
  // How about iterate over records and delete each?
  // There's a few takeaway you should know of
  // 1. API Operation with DB is quite expensive
  // 2. So each operation is still heavy no matter what how many called
  // 3. That's why Operating thru whole record is not good
  // Solution == Find a way to execute all operation at once
  // ex) Collection based operation
  // Operation with DB == Net execution + connecting overhead

  // So how to solve this efficiently?
  // == Mongo update operator
  // Refer to update_test.js

                              // this === joe
  BlogPost.remove({ _id: { $in: this.blogPosts }})
  // How this works?
  // 1. Go to BlogPost collection
  // 2. Look at all there _id
  // If the _id is in this.blogPosts, remove it
    .then(()=>next());
    // Other registered middleware will be called only after next

});

// Making 'users' collection in MongoDB
const User = mongoose.model('user', UserSchema);

module.exports=User;
