const assert = require('assert');
const User = require('../src/user');

describe('Subdocuments',()=>{
  it('can create a subdocument',(done)=>{
    const joe = new User({
      name:'Joe',
      posts:[{ title:'NodeJS and MongoDB'}]
    });

    joe.save()
      .then(()=>User.findOne({ name: 'Joe'}))
      .then((user)=>{
        assert(user.posts[0].title === 'NodeJS and MongoDB');
        done();
      });
  });

  it('can add subdocuments to existing record',(done)=>{
    const joe = new User({
      name:'Joe',
      posts:[]
    });

    joe.save()
    // .then(()=>{return User.findOne({ name: 'Joe'})})
      .then(()=>User.findOne({ name: 'Joe'}))
      .then((user)=>{
        user.posts.push({ title: 'New Post'});
        // we can do chained-on functioning by hands in hands of Promise
        // Returning user.save() returns Promise obect
        return user.save();
      })
      .then(()=>User.findOne({ name: 'Joe'}))
      .then((user)=>{
        assert(user.posts[0].title === 'New Post');
        done();
      });
  });

  it('can remove an existing subdocument',(done)=>{
    const joe = new User({
      name:'Joe',
      posts: [{title:'New title'}]
    });

    joe.save()
      .then(() => User.findOne({name:'Joe'}))
      .then((user) =>{
        const post = user.posts[0];
        post.remove();
        return user.save();
      })
        .then(()=>User.findOne({name:'Joe'}))
        .then((user)=>{
          assert(user.posts.length ===0);
          done();
        })
  });
});
