/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
*/

function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

function howManyWays(matrix) {
  //build a tree, with left and right node
  //after create a tree , print all path from root to leave
  //if path.length === n + m, counter++
  //return counter
  let tree = buildTree(0, 0, matrix);
  let str = '';
  let arr = [];
  printAllPath(tree, str, arr);
  console.log(arr);
  let standard = '0'.repeat(matrix.length + matrix[0].length - 1);

  let counter = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === standard) counter++;
  }
  return counter;
}

function printAllPath(node, str, arr) {
  if (!node.left && !node.right) arr.push(str + node.val);
  if (node.left) printAllPath(node.left, str + node.val, arr);
  if (node.right) printAllPath(node.right, str + node.val, arr);
}
