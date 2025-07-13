#!/usr/bin/node
const { argv } = require('node:process');
const fact = parseInt(argv[2]);

function factorial (n) {
  if (n === 0) { // Base case
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(fact));
