var fs = require('fs');
var readline = require('readline');

// var fileName = 'file1.txt'
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Input filename: ", function(fileName) {
  fs.readFile(fileName, function (error, buffer) {
    if (error) {
      console.log(error.message);
      rl.close();
      return;
    }
    var contents = buffer.toString();
    var caps = contents.toUpperCase();
    console.log('File data in caps: ', caps);
  });
  rl.close();
});
