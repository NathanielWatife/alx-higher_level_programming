#!/usr/bin/node

const arg = process.argv[2];

const sizeSquare = parseInt(arg, 10);

if (!isNaN(sizeSquare)) {
  let i = 0;
  while (i < sizeSquare) {
    let row = '';
    let j = 0;
    while (j < sizeSquare) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
