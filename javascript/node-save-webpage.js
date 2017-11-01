var fs = require('fs');
var readline = require('readline');
var request = require('request');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('URL: ', function(url) {
  request.get(url, function (error, response, html) {
    if (error) {
      console.log(error.message);
      return;
    }
    rl.question('Save to filename: ', function(fileName) {
      rl.close();
      fs.writeFile(fileName, html, function(error) {
        if (error) {
          console.log(error.message);
          return;
        }
        console.log('HTML save to: ', fileName);
      })
    })
  });
});
