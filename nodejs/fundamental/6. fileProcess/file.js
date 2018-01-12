var fs = require('fs');

// __dirname = path of this location
var greet = fs.readFileSync(__dirname+'/greet.txt','utf8');
// readFileSync == before move on to next line,
// it will wait until buffer is filled up
// useful when loading configuration

console.log(greet);

var greet2=fs.readFile(__dirname+'/greet.txt','utf8',
function(err,data){
    console.log(data);
});
// When readFile is finished by OS,
// please run latter callback function code
// if no running code because JS is synchronous


// below code appears first then readFile
// because Node is asynchronous
console.log('Done !');

// require -> readFileSync -> Done!        
//                         -> readFile

// takeaway = 
// when file is large, it seems good not to use Sync
// If asynchronous is available, use it.