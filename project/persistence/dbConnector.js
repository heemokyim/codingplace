const mysql = require('mysql');

var dbConn = mysql.createConnection({
  host:'localhost',
  user:'root',
  password:'5555',
  database:'initial_portfolio'
});
// config 파일 반영

let Users_SQL ="CREATE TABLE IF NOT EXISTS users (name  VARCHAR(10));";
// let sql = "11 \ 11" 로 수정

dbConn.query(Users_SQL,(err,rows)=>{
  if(err) throw err;
  console.log('DB connected !');
})

module.exports = dbConn;
