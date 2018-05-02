const admin_config = require('/home/ej/github/mongo_db_config.json')

module.exports = {
  getAdminConnection: function(){
    return `mongodb://${admin_config.ID}:${admin_config.PW}@localhost/tmp?authSource=admin`
  }
}
