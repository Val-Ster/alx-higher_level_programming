#!/usr/bin/node

// Define the factorial function
function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Get the first argument from the command line and convert it to an integer
const arg = parseInt(process.argv[2]);

// Print the result of the factorial computation
console.log(factorial(arg));
