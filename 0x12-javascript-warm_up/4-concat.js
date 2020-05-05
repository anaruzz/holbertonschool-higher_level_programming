#!/usr/bin/node
// a script that prints two arguments passed to it in a format
let arg1 = 'undefined';
let arg2 = 'undefined';
if (process.argv.length < 4) {
  arg1 = process.argv[2];
} else {
  arg1 = process.argv[2];
  arg2 = process.argv[3];
}
console.log(arg1 + ' is ' + arg2);
