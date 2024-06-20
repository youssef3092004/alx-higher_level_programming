#!/usr/bin/node
const process = require('process');
const input = parseInt(process.argv[2], 10);
if (!isNaN(input)) {
  for (let i = 0; i < input; i++) {
    let row = '';
    for (let j = 0; j < input; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
