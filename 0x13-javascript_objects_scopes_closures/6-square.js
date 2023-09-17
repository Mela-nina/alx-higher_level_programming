#!/usr/bin/node

// This is a class Square that defines a square and inherits from Square of 5-square.js

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let j = 0; j < this.height; j++) console.log(c.repeat(this.width));
    }
  }
};
