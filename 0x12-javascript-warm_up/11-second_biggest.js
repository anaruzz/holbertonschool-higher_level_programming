#!/usr/bin/node
// a script that searches the second biggest integer in the arguments
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let i = 3; let current;
  let max1 = parseInt(process.argv[2]);
  let max2 = parseInt(process.argv[2]);
  for (; i < process.argv.length; i++) {
    current = parseInt(process.argv[i]);
    if (current > max1) {
      max2 = max1;
      max1 = current;
    }
    if (current > max2 && current < max1) {
      max2 = current;
    }
  }
  console.log(max2);
}
