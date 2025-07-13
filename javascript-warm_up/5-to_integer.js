#!/usr/bin/node
const { argv } = require('node:process');

// convert the argument to a number
const arg = parseInt(argv[2]);

// Check if it's a valid number
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number:', arg);
}
