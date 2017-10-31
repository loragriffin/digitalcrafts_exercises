function box(w, h) {
  // printing top row
  var fullrow = '*'.repeat(w);
  console.log(fullrow);

  // printing middle section
  var middle = '*' + ' '.repeat(w - 2) + '*'
  for (var i = 0; i < h - 2; i++) {
    console.log(middle);
  }

  // print bottom row
  console.log(fullrow);
}

box(12, 6);
