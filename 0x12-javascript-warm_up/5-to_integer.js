#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(arg)) {
  console.log(`My number: ${parseInt(arg)}`);
} else {
  console.log('Not a number');
}
/* I can also use
if (!isNaN(process.argv[2])) {
  console.log(`My number: ${parseInt(process.argv[2])}`);
} else {
  console.log('Not a number');
}
*/
