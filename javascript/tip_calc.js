var bill
var service
var tip
var total

function tipCalc (bill, service) {
  if (service == 'good') {
    tip = bill * 0.2;
    total = bill + tip;
    console.log("Bill amount: $" + bill);
    console.log("Recommended Tip: $" +  tip);
    console.log("Total: $" +  total);
  }
  else if (service == 'fair') {
    tip = bill * 0.15;
    total = bill + tip;
    console.log("Bill amount: $" + bill);
    console.log("Recommended Tip: $" +  tip);
    console.log("Total: $" +  total);
  }
  else if (service == 'bad') {
    tip = bill * 0.1;
    total = bill + tip;
    console.log("Bill amount: $" + bill);
    console.log("Recommended Tip: $" +  tip);
    console.log("Total: $" +  total);
  }
}


tipCalc(10, 'good');
