#!/usr/bin/node

// Get the arguments passed to the script, excluding the first two (node and script path)
const args = process.argv.slice(2).map(Number);

// Check if there are fewer than 2 arguments
if (args.length <= 1) {
  console.log(0);
} else {
  // Sort the arguments in descending order
  args.sort((a, b) => b - a);
  // Print the second biggest integer
  console.log(args[1]);
}
