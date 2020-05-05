#!/usr/bin/node
// a script that adds the first two arguments
function add(a, b) {
  return a + b;
}
let a = parseInt(process.argv[2])
let b = parseInt(process.argv[3])
console.log(add(a, b));
