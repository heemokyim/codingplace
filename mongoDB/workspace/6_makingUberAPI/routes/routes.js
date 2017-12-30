const DriversController = require('../controllers/drivers_controller')

// module.exports = function(){}
module.exports = (app) => {

  // Watch for incoming requests of method GET
  // to the route http://localhost:3050/api

  app.get('/api', DriversController.greeting);

  app.post('/api/drivers', DriversController.create);

};
