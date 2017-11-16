const mongoose = require('mongoose');
const assert = require('assert');
const User = require('../src/user');
const Comment = require('../src/comment');
const BlogPost = require('../src/blogPost');

// upper case = Model, collection
// lower case = Instance

describe('Associations', ()=>{
  let joe,blogPost,comment;

  beforeEach((done)=>{
    joe = new User({ name: 'Joe' });
    blogPost = new BlogPost({ title: 'JS is Great', content: 'Yep it really is' });
    comment = new Comment({ content: 'Congrats on great post' });

    // Looks like sub-document nesting but it's not
    joe.blogPosts.push(blogPost);
    blogPost.comments.push(comment);
    comment.user = joe;

    // joe.save(); -> this is promise
    // blogPost.save(); -> this is promise
    // comment.save(); -> this is promise
    // ** What's problem doing like upper?
    // NodeJS is asynchronous, so saving order can be at random.
    // And what if saving order is critical for persistence ?
    // How can we solve this?
    // Promise.all()
    // https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/all

    // Execute every component as input order
    // 1. joe.save() -> blogPost.save() -> comment.save()
    // 2. If all promises are completed, Do then()
    // 3. Why Promise.all ? ==> saving order is critical
    Promise.all([joe.save(), blogPost.save(), comment.save()])
      .then(()=>done());
  });

  // it.only == only running this test
  // xit == pending this test
  it('saves a relation between a user and a blogpost',(done)=>{
    User.findOne({ name: 'Joe'})
      // resolve User instance with blogPosts == User.blogPosts
      // ==> load up actual data from ObjectId
      // Is there any way to load up recursively?
      // ==> In mongoose, NO !
      .populate('blogPosts')
      .then((user)=>{
        assert(user.blogPosts[0].title === 'JS is Great');

        // see the difference without populate modifier by console.log(user)
        // console.log(user);
        done();
      });
  });

  // navigating deeply nested property
  it('saves a full relation tree (nesting)',(done)=>{
    User.findOne({name :'Joe'})
      .populate({
        // find User.blogPosts
        path:'blogPosts',

        // Among properties inside of User.blogPosts,
        populate:{
          // find User.blogPosts.comments
          path: 'comments',
          model: 'comment',
          // name of stored collection

          populate:{
            path:'user',
            model:'user'
          }
        }
      })
      .then((user)=>{
        // console.log(user.blogPosts[0]);
        // console.log();
        // console.log(user.blogPosts[0].comments[0]);
        assert(user.name === 'Joe');
        assert(user.blogPosts[0].title === 'JS is Great');
        assert(user.blogPosts[0].comments[0].content === 'Congrats on great post');
        assert(user.blogPosts[0].comments[0].user.name === 'Joe');
        done();
      });
  });
});
