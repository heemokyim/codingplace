const mongoose = require('mongoose')
const config = require('./get_config')

const User = require('./models/person')

mongoose.Promise = global.Promise;
mongoose.connect(config.getAdminConnection());

var joe = new User({ name:'Joe'})

joe.save()
  .then(()=>{
    console.log('User saved successfully !')
  })
  .catch(()=>{
    console.log('Error occured')
  })
