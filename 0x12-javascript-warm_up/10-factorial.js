#!/usr/bin/node
// a script that adds the first two arguments
function factorial(a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}
const n = parseInt(process.argv[2]);
console.log(factorial(n));
