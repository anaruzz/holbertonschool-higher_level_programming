#!/usr/bin/node
// a script that prints two arguments passed to it in a format
if (process.argv.length < 3) {
  console.log('Not a number');
} else {
  const a = parseInt(process.argv[2]);
  if (isNaN(a)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + a);
  }
}
