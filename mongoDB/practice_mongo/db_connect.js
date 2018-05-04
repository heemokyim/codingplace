const mongoose = require('mongoose')
const config = require('./get_config')

const User = require('./models/user')

mongoose.Promise = global.Promise;
mongoose.connect(config.getAdminConnection());

var joe = new User({ name:'Jo'})

console.log(joe._id)
