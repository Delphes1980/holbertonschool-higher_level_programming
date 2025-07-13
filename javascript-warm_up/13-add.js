#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

module.exports.add = add;
