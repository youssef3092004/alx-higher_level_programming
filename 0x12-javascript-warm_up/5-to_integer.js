#!/usr/bin/node
const process = require('process');
if (!process.argv[2]) {
  console.log('Not a number');
} else {
  let num = parseInt(process.argv[2]);
  if (!isNaN(num)) {
    num = String(num);
    console.log(`My number: ${num}`);
  } else {
    console.log('Not a number');
  }
}
