#!/usr/bin/node
const { argv } = require('node:process');
const arg1 = argv[2];
const arg2 = argv[3];

const text = arg1 + (' is ') + arg2;
console.log(text);
