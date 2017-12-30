const Driver = require('../models/driver');

module.exports = {
  // greeting : function(req,res) {}

  greeting(req, res) {
    res.send({hi:'there'})
  },

  create(req, res) {
    console.log(req.body);
  }
};
