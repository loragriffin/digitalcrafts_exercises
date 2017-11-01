var fs = require('fs');
var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Input filename: ", function(fileName) {
  rl.close();
  fs.readFile(fileName, function (error, buffer) {
    if (error) {
      console.log(error.message);
      return;
    }
    var contents = buffer.toString();
    var caps = contents.toUpperCase();
    console.log('File data in caps: ', caps);
  });
});
