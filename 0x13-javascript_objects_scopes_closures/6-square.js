#!/usr/bin/node
// Script that creates square
const Rectangle = require('./5-square');
class Square extends Rectangle {
  // charPrint
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Square;
