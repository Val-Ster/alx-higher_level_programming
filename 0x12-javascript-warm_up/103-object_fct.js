#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};

console.log(myObject);

// Call the incr function to increment the value
myObject.incr();
console.log(myObject);

// Call the incr function again
myObject.incr();
console.log(myObject);

// Call the incr function once more
myObject.incr();
console.log(myObject);
