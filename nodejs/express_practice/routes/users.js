var express = require('express');
var router = express.Router();

/* GET users listing. */
// every endpoint starting with '/users'
router.get('/ii', function(req, res, next) {
  res.send('respond with a resource');
});

router.post('/person',function(req,res,next){
  res.send(req.body.first + req.body.last);
});

router.post('/person1',function(req,res,next){
  res.send(req.body.firstname + req.body.lastname);
});

router.post('/personjson',function(req,res,next){
  console.log(req.body.firstname);
  console.log(req.body.lastname);
  console.log(req.body);
  console.log(req.firstname);
  console.log(req.lastname);
});

module.exports = router;
