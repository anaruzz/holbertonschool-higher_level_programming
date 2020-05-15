#!/usr/bin/node
// Script that creates empty class

class Rectangle {
  constructor (h, w) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print
  print () {
    var i, j;
    for (i = 0; i < this.width; i++) {
      for (j = 0; j < this.height; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Rectangle;
