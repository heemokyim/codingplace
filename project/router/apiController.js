const bodyParser=require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false });
const jsonParser = bodyParser.json();

let dbConn = require('../persistence/dbConnector');

module.exports=function(app){
  app.get('/users/:name',function(req,res){

    // SQL = "INSERT INTO users VALUES ('"++"');'"

    console.log(req);
    console.log(req.body);
    console.log(req.query.qstr);

    // dbConn.query(SQL,function(err,rows){
    //   if(err) throw err;
    //   console.log(rows);
    // });

    res.send('User saved !');
  });

  app.get('/userss',function(req,res){

    // dbConn.query(SQL,function(err,rows){
    //   if(err) throw err;
    //   console.log(rows);
    // });
  });
};
