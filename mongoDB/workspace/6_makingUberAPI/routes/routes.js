const DriversController = require('../controllers/drivers_controller')

// module.exports = function(){}
module.exports = (app) => {

  // Watch for incoming requests of method GET
  // to the route http://localhost:3050/api

  app.get('/api', DriversController.greeting);

  app.post('/api/drivers', DriversController.create);

  app.put('/api/drivers/:id', DriversController.edit);
  // By convention, modifier ID is putted in URL
  // But we can also put in http body

  app.delete('/api/drivers/:id', DriversController.delete);

  app.get('/api/drivers', DriversController.index);
};
