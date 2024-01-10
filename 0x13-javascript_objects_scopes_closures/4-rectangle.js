#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  // start of print
  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
  // end of print

  // start of rotate
  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }
  // end of rotate

  // start double
  double () {
    this.width *= 2;
    this.height *= 2;
  }
  // end of double
}
module.exports = Rectangle;
