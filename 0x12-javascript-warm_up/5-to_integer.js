#!/usr/bin/node

const myArg = process.argv[2];
const myInt = parseInt(myArg, 10);

if (!isNaN(myInt)) {
  console.log(`My number: ${myInt}`);
} else {
  console.log('Not a number');
}
