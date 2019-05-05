/*
Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
*/

class Matrix {
  constructor(arr) {
    this.arr = arr;
  }
  next() {
    if (!this.arr.length) return 'No more elements!';
    while (!this.has_next()) {
      this.arr.shift();
    }
    this.arr.shift().map(el => console.log(el));
    // return this.arr[0].shift();
  }
  has_next() {
    return this.arr[0].length ? true : false;
  }
}

let returnNext = new Matrix([[1, 2], [3], [], [4, 5, 6], [7]]);

returnNext.next();
returnNext.next();
returnNext.next();
returnNext.next();
returnNext.next();
returnNext.next();
