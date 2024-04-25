#!/usr/bin/node

// Get the number of occurrences from the command-line argument
let numOccurrences = parseInt(process.argv[2]);

// Check if the argument is a valid number
if (!isNaN(numOccurrences)) {
    // Print "C is fun" the specified number of times using a loop
    for (let i = 0; i < numOccurrences; i++) {
        console.log("C is fun");
    }
} else {
    // Print an error message if the argument is not a valid number
    console.log("Missing number of occurrences");
}
