const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const CommentSchema = new Schema({
  content: String,
  user: { type: Schema.Types.ObjectId, ref: 'user'}
  // what to put in ref == name of stored collection
  // 'user' for User collection
  // 'blogpost' for BlogPost collection
  // 'comment' for Comment collection
});

const Comment = mongoose.model('comment',CommentSchema);

module.exports = Comment;
