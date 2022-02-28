#!/usr/bin/node
// This script prints x times "C is fun"
if ((isNaN(process.argv[2])) === false) {
    for (let num = 0; num < parseInt(process.argv[2]); num++){
	console.log('C is fun');
    }
	} else {
	    console.log('Missing number of occurrences');
	}
