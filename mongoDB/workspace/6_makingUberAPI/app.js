const express = require('express');
const bodyParser = require('body-parser');
const routes = require('./routes/routes');
const app = express();


app.use(bodyParser.json());
// Invoking middle-ware
// Before reaching to any router or controller,
// convert any html body part into json format
// type(req.body) == JSON

routes(app);

module.exports = app;
