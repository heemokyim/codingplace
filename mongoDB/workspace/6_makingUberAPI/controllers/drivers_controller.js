const Driver = require('../models/driver');

module.exports = {
  // greeting : function(req,res) {}

  greeting(req, res) {
    res.send({hi:'there'})
  },

  create(req, res, next) {
    const driverProps = req.body;

    Driver.create(driverProps)
      .then(driver => res.send(driver))
      // It returns driver document to client only when successfully created
      .catch(next);
      // If error, just call next middleware in app.use of app.js
  },

  edit(req, res, next) {
    const driverId = req.params.id;
    const driverProps = req.body;

    Driver.findByIdAndUpdate({ _id: driverId}, driverProps)
      .then(() => Driver.findById({ _id: driverId}))
      .then(driver => res.send(driver))
      .catch(next);
  },

  delete(req, res, next) {
    const driverId = req.params.id;

    Driver.findByIdAndRemove({ _id: driverId})
      .then(driver => res.status(204).send(driver))
      // driver is removed document
      .catch(next);
  }
};
