var bodyParser = require('body-parser');

module.exports = function(app) {

    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({ extended: true }));


    app.post('/api/todo', function(req, res) {
        console.log(req)
    });
}
