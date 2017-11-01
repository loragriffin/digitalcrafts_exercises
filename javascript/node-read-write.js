var fs = require('fs');
var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Input filename: ", function(inputFile) {
  rl.question('Ouput filename: ', function(outputFile) {
    rl.close();
    fs.readFile(inputFile, function (error, buffer) {
      if (error) {
        console.log(error.message);
        return;
      }
      var contents = buffer.toString();
      var caps = contents.toUpperCase();
      fs.writeFile(outputFile, caps, function(error) {
        if (error) {
          console.log(error.message);
          return;
        }
        console.log('New file saved: ', outputFile);
        fs.readFile(outputFile, function (error, buffer) {
          if (error) {
            console.log(error.message);
            return;
          }
          var contents = buffer.toString();
          console.log('Contents: ', buffer.toString());
        });
      });
    });
  });
});
