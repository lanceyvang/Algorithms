/*
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, 
replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes
B B G
G G G
G G G
B B B
*/

const replace = (matrix, location, newColor) => {
  let [x, y] = location;
  let sampleColor = matrix[x][y];

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (matrix[i][j] === sampleColor) matrix[i][j] = newColor;
    }
  }
  return matrix;
};

let arr = [['B', 'B', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W'], ['B', 'B', 'B']];
console.log(replace(arr, [2, 2], 'G'));
