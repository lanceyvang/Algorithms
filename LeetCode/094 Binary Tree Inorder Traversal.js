/*
94. Binary Tree Inorder Traversal
Medium

1506

65

Favorite

Share
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
*/
function TreeNode(val) {
  this.val = val;
  this.left = null;
  this.right = null;
}
let root = new TreeNode(1);
root.left = null;
root.right = new TreeNode(2);
root.right.left = new TreeNode(3);

function inorderTraversal(root) {
  const stack = [];
  const results = [];

  while (root || stack.length) {
    if (root) {
      stack.push(root);
      root = root.left;
    } else {
      root = stack.pop();
      results.push(root.val);
      root = root.right;
    }
  }
  return results;
}

function recursive(node) {
  let arr = [];
  makeArr(node);
  return arr;

  function makeArr(node) {
    if (node) {
      makeArr(node.left);
      arr.push(node.val);
      makeArr(node.right);
    }
  }
}

console.log(iterative(root)); // => 1
// console.log(recursive(root));
