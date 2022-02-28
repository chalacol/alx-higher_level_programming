#!/usr/bin/node
// The script computes and prints a factorial
function factorial(a) {
    if (a === 1) {
	return 1;
    } else {
	return a * factorial(a - 1);
    }
}
if (isNaN(process.argv[2])) {
    console.log(factorial(1));
} else if (parseInt(process.argv[2]) >= 1) {
    console.log(factorial(parseInt(process.argv[2])));
}
