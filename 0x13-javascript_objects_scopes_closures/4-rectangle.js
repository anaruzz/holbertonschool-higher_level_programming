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

  // rotate
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // double
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
