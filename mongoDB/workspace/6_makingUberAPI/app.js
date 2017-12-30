const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const routes = require('./routes/routes');
const app = express();

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/muber',{useMongoClient:true});

app.use(bodyParser.json());
// Invoking middle-ware for POST method
// Before reaching to any router or controller,
// convert any html body part into json format
// type(req.body) == JSON

routes(app);

module.exports = app;
