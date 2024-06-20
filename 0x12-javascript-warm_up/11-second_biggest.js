#!/usr/bin/node

const process = require('process');
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  let fstgreater = Number(process.argv[2]);
  let secgreater = Number(process.argv[3]);
  for (let i = 2; i < len; i++) {
    if (fstgreater < Number(process.argv[i])) {
      fstgreater = Number(process.argv[i]);
    }
  }
  for (let i = 2; i < len; i++) {
    if (secgreater < Number(process.argv[i]) && secgreater < fstgreater) {
      if (Number(process.argv[i]) < fstgreater) {
        secgreater = Number(process.argv[i]);
      }
    }
  }
  console.log(secgreater);
}
