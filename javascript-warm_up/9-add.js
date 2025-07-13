#!/usr/bin/node
const { argv } = require('node:process');
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

function add (a, b) {
  if (a !== isNaN(a) && b !== isNaN(b)) {
    const result = a + b;
    console.log(result);
  }
}

add(num1, num2);
