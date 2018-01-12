var moment = require('moment');
// first, require searches core of node for 'moment'
// second, it searches 'moment' folder in node_modules

console.log(moment().format("YYYY-MM-DD"));
