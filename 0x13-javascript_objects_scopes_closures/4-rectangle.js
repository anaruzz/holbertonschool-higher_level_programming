#!/usr/bin/node
// Script that creates empty class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
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
