const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const BlogPostSchema = new Schema({
  title:String,
  content:String,
  comments: [{
    type: Schema.Types.ObjectId,
    // find out more by console.log(Schema.Types)
    ref: 'comment'
  }]
  // what to put in ref == name of stored collection
  // 'user' for User collection
  // 'blogpost' for BlogPost collection
  // 'comment' for Comment collection
},{usePushEach:true});

const BlogPost = mongoose.model('blogPost',BlogPostSchema);

module.exports = BlogPost;
