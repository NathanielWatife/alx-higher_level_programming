#!/usr/bin/node

const myArg = process.argv[2];
const myInt = parseInt(myArg, 10);

if (!isNaN(myInt)) {
  let i = 0;
  while (i < myInt) {
	console.log('C is fun');
	i++;
  }
} else {
  console.log('Missing number of occurrences');
}
