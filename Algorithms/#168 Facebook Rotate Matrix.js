/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?
*/
const matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

const rotate = matrix => {
  let counter = 1;

  for (let i = matrix.length - 1; i >= 0; i--) {
    for (let j = 0; j < matrix.length; j++) {
      matrix[j][i] = counter;
      counter++;
    }
  }
  return matrix;
};

console.log(rotate(matrix));
