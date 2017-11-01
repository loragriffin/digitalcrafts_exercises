var readline = require('readline');
var dns = require('dns');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Domain name: ", function(answer) {
  var ip = dns.lookup(answer, function (error, address, family) {
    if (error) {
      console.log(error.message);
      return;
    }
    console.log('IP address: ', address);
  });
  rl.close();
});
