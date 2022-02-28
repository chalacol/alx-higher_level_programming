#!/usr/bin/node
// This script prints a square
if ((isNaN(process.argv[2])) === false) {
    let line = '';
    for (let num = 0; num < parseInt(process.argv[2]); num++) {
	line += 'X';
    }
    for (let num = 0; num < parseInt(process.argv[2]); num++) {
	console.log(line);
    }
} else {
    console.log('Missing size');
}
