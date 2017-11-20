const bodyParser=require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false });
const jsonParser = bodyParser.json();

let dbConn = require('../persistence/dbConnector');

module.exports=function(app){

  // 000. User Sign up
  app.get('/users/',function(req,res){
    console.log(req.query);
    let args = req.query;
    let SQL = `INSERT INTO users(ID,PW) VALUES('${args.id}','${args.pw}');`;
    SQL += 'SELECT pid FROM users WHERE pid = LAST_INSERT_ID();';

    dbConn.query(SQL,(err,rows)=>{
      if(err){
        res.send(JSON.stringify({
          msg:'Error while sign up',
          code:'000 Sign up',
        }));

        throw err;
      }

      res.send(JSON.stringify({
        msg:`User sucessfully created !`,
        result:rows[1][0]
      }));
    });
  });

  // 001. Find User
  app.get('/users/:id',function(req,res){
    let ID = req.params.id;
    let SQL = `SELECT pid FROM users WHERE ID='${ID}';`

    // rows, results 차이 = results로 하면 서버가 에러를 캣치못하고 죽음
      dbConn.query(SQL,(err,rows)=>{
        if(err){
          res.send(JSON.stringify({
            msg:'Error while find ID = '+ID,
            code:'001 Find user'
          }));

          throw err;
        }

        res.send(JSON.stringify({
          msg:'User succecssfuly found',
          result:rows
        }))
      });

  });
};
