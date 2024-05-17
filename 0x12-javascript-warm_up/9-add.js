#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Get the first and second arguments from the command line
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

// Check if both arguments are valid numbers
if (isNaN(firstArg) || isNaN(secondArg)) {
  console.log('NaN');
} else {
  // Print the result of the addition
  console.log(add(firstArg, secondArg));
}
