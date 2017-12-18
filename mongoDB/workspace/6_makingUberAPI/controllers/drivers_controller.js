

module.exports = {
  // greeting : function(req,res) {}
  greeting(req, res) {
    res.send({hi:'there'})
  },

  create(req, res) {
    console.log(req.body);
    res.send({ hi: 'there' });
  }
};
