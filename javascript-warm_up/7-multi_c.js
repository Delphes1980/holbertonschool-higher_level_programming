#!/usr/bin/node
const { argv } = require('node:process');
const line = 'C is fun';
const arg = parseInt(argv[2]);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < arg; i++) {
    console.log(line);
}
}
