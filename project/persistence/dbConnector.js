const mysql = require('mysql');
const config = require('./config')

var dbConn = mysql.createConnection({
  host:config.HOST,
  user:config.USER,
  password:config.PASSWORD,
  database:config.DATABASE,
  multipleStatements:true
});

let TableUsersSQL ="CREATE TABLE IF NOT EXISTS users (\
  pid INT NOT NULL AUTO_INCREMENT, \
  ID VARCHAR(30) NOT NULL,\
  PW VARCHAR(30) NOT NULL,\
  PRIMARY KEY (pid)\
  );\
";
// let sql = "11 \ 11" 로 수정

dbConn.query(TableUsersSQL,(err,rows)=>{
  if(err) throw err;
  console.log('DB connected !');
})

module.exports = dbConn;
