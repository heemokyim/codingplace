// post schema is netsted inside user schema
// When nested, post is called sub-document or sub-collection

const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const PostSchema = new Schema({
  title:String
});

module.exports = PostSchema;
