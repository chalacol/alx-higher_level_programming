#!/usr/bin/node
// This script converts the first argument passed to it to integer and prints it
if ((isNaN(process.argv[2])) === false) {
    console.log('My number: ' + parseInt(process.argv[2]));
} else {
    console.log('Not a number');
}
