#!/usr/bin/node

//This is a script that prints a square

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let s = 0; s < size; s++) {
    let row = '';
    for (let d = 0; d < size; d++) row += 'X';
    console.log(row);
  }
}
