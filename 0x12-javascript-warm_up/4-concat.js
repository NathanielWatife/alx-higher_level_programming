#!/usr/bin/node

const firstLine = process.argv[2];
const secondLine = process.argv[3];

if (firstLine !== undefined && secondLine !== undefined) {
  console.log(`${firstLine} is ${secondLine}`);
} else {
  console.log('Undefined is Undefined');
}
