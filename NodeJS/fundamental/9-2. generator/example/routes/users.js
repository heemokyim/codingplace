var express = require('express');
var router = express.Router();

/* GET users listing. */
// localhost:3000/users/1234
router.get('/1234', function(req, res, next) {
  res.send('respond with a resource1234');
});

module.exports = router;
