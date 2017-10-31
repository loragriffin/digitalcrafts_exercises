// function rewrites

// example 1
function add(x, y) {
  var result = x + y;
  return result;
}

// rewritten as a callback
function add(x, y) {
  var result = x + y;
  callback(result);
}

// example 2
function subtract(x, y) {
  return x - y;
}

// rewritten as a callback
function subtract(x, y) {
  var result = x - y;
  callback(result);
}

// example 3
function greeting(person) {
  return 'Hola, ' + person + '!';
}

// rewritten as a callback
function greeting(person) {
  var result = 'Hola, ' + person + '!';
  callback(result);
}

// example 4
function product(numbers) {
  return numbers.reduce(function(a, b) {
    return a * b;
  }, 1);
}

// rewritten as a callback
function product(numbers) {
  
}
