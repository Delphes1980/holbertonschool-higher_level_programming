#!/usr/bin/node
const { argv } = require('node:process');
// const arg = [parseInt(argv.length)];

const biggest = [];
for (let i = 2; i < argv.length; i++) {
  const convertArg = parseInt(argv[i]);
  /* Check if it's not a NaN before putting it in the array */
  if (convertArg !== isNaN(convertArg)) {
    biggest.push(convertArg);
  }
}
/* Check if there's at least 2 numbers */
if (biggest.length < 2) {
  console.log('0');
} else {
  /* Sort the array from the biggest to the lowest */
  const sortedArg = biggest.sort(function (a, b) {
    return b - a;
  });
  console.log(sortedArg[1]);
}
