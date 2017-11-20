const bodyParser=require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false });
const jsonParser = bodyParser.json();

let dbConn = require('../persistence/dbConnector');

module.exports=function(app){
  app.get('/users/',function(req,res){
    console.log(req.query);
    let args = req.query;
    let SQL = `INSERT INTO users(ID,PW) VALUES('${args.id}','${args.pw}');`;
    SQL += 'SELECT pid FROM users WHERE pid = LAST_INSERT_ID();';

    dbConn.query(SQL,(err,results)=>{
      if(err){
        res.send(JSON.stringify({
          msg:'Error while sign up',
          code:'000 Sign up'
        }));

        throw err;
      }
      // console.log(results)
      res.send(JSON.stringify({
        msg:`User sucessfully created !`,
        pid:results[1][0].pid
      }));
    });
  });

  app.get('/users/:id',function(req,res){
    let ID = req.params.id;
    let SQL = `SELECT pid FROM users WHERE ID='${ID}';`

    // results, rows 차이
      dbConn.query(SQL,(err,rows)=>{
        if(err) throw err;

        res.send(JSON.stringify({
          msg:'User succecssfuly found',
          result:rows
        }))
      });

  });
};
