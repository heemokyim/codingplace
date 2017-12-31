const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const routes = require('./routes/routes');
const app = express();

mongoose.Promise = global.Promise;
if(process.env.NODE_ENV !== 'test') {
  mongoose.connect('mongodb://localhost/muber',{useMongoClient:true});
}
// if not implemented like this,
// muber and muber_test database will be connected
// which has no meaning of using NODE_ENV

app.use(bodyParser.json());
// Invoking middle-ware for POST method
// Before reaching to any router or controller,
// convert any html body part into json format
// type(req.body) == JSON

routes(app);

app.use((err, req, res, next) => {
  res.status(422).send({error: err.message});
});
// Refer to 10_Middleware
// For middleware to go on chaining,
// Each of middleware explicitly call next()
// Catch promise of any code will be designated here
// Ex) create.catch in drivers_controller.js

// *********************************************
// 1. With no error
// bodyParser.json() -> routes(app)
// 2. With error
// bodyParser.json() -> routes(app) -> res.status(422).send()
// *********************************************

module.exports = app;
