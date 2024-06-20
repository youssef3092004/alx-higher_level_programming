#!/usr/bin/node

const process = require('process');
const input = parseInt(process.argv[2], 10);
function factorial (num) {
  if (isNaN(num) || num < 0) {
    console.log('Invalid input');
    return;
  }
  if (num === null) {
    console.log(1);
    return;
  }
  let fact = 1;
  for (let i = 1; i <= num; i++) {
    fact *= i;
  }
  console.log(fact);
}
if (isNaN(input)) {
  console.log(1);
} else {
  factorial(input);
}
