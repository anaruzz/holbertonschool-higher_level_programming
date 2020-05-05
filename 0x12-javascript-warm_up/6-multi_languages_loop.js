#!/usr/bin/node
// Script that prints 3 lines with a loop
const arr = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let line;
for (line in arr) {
  console.log(arr[line]);
}
