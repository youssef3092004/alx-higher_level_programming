#!/usr/bin/node
const process = require('process');
const input1 = parseInt(process.argv[2], 10);
const input2 = parseInt(process.argv[3], 10);
function add (a, b) {
  console.log(a + b);
}
add(input1, input2);
