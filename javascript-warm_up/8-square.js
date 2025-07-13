#!/usr/bin/node
const { argv } = require('node:process');
const toPrint = 'X';
const arg = parseInt(argv[2]);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let Printable = '';
    for (let j = 0; j < arg; j++) {
      Printable += toPrint;
    }
    console.log(Printable);
  }
}
