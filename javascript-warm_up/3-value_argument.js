#!/usr/bin/node
const { argv } = require('node:process');

if (argv[2] == null) {
  console.log('No argument');
} else {
  for (let i = 0; i > argv[2]; i++) {
    console.log(i);
  }
}
