var express = require('express');
var app = express();
var setupController = require('./controllers/setupController');
var apiController = require('./controllers/apiController');

var port = process.env.PORT || 3000;

mongoose.Promise=global.Promise;

setupController(app);
apiController(app);

app.listen(port);
