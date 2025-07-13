#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

exports.add = add;

const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

if (num1 !== isNaN(num1) && num2 !== isNaN(num2)) {
  const result = add(num1, num2);
  console.log(result);
}
