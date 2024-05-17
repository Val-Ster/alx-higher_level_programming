#!/usr/bin/node

// Define the function addMeMaybe
function addMeMaybe (number, theFunction) {
  // Increment the number
  const incrementedNumber = number + 1;

  // Call the callback function with the incremented number
  theFunction(incrementedNumber);
}

// Export the addMeMaybe function
module.exports = { addMeMaybe };
