/*
Given the root node of a binary search tree (BST) and a value to be 
inserted into the tree, insert the value into the BST. Return the root
node of the BST after the insertion. It is guaranteed that the new value
does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long
as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
*/
function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}
let root = new TreeNode(4);
root.left = new TreeNode(2);
root.right = new TreeNode(7);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(3);

var insertIntoBST = function(root, val) {
  insert(root, val);
  return root;

  function insert(node, val) {
    if (node) {
      if (val < node.val && !node.left) {
        node.left = new TreeNode(val);
      } else if (val > node.val && !node.right) {
        node.right = new TreeNode(val);
      }
      if (val < node.val) insert(node.left, val);
      if (val > node.val) insert(node.right, val);
    }
  }
};

console.log(insertIntoBST(root, 9));

var insertIntoBST = function(root, val) {
  let newNode = new TreeNode(val);
  if (!root.left && val < root.val) root.left = newNode;
  if (!root.right && val > root.val) root.right = newNode;

  if (val > root.val) insertIntoBST(root.right, val);
  if (val < root.val) insertIntoBST(root.left, val);

  return root;
};
