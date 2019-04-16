/*
Random Node: You are implementing a binary tree class from scratch which, 
in addition to insert, find, and delete, has a method getRandomNode() which returns a random node from the tree.
All nodes should be equally likely to be chosen.Design and implement an algorithm for getRandomNode, 
and explain how you would implement the rest of the methods.
*/

/*
Random Node: You are implementing a binary tree class from scratch which, 
in addition to insert, find, and delete, has a method getRandomNode() 
which returns a random node from the tree.
All nodes should be equally likely to be chosen.
Design and implement an algorithm for getRandomNode, 
and explain how you would implement the rest of the methods.
*/

//

function TreeNode(val) {
  this.val = val;
  this.left = null;
  this.right = null;
}

TreeNode.prototype.getRandomNode = function() {
  let arr = [];
  inorder(this, arr);
  return arr[Math.floor(Math.random() * arr.length)];
};

TreeNode.prototype.find = function(target) {
  let arr = [];
  inorder(this, arr);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].val === target) return arr[i];
  }
};

TreeNode.prototype.insert = function(value) {
  if (value > this.val && this.right) this.right.insert(value);
  if (value < this.val && this.left) this.left.insert(value);
  if (value > this.val && !this.right) this.right = new TreeNode(value);
  if (value < this.val && !this.left) this.left = new TreeNode(value);
};

TreeNode.prototype.delete = function(target) {
  let arr = [];
  inorder(this, arr);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].val === target) return arr[i];
  }
};

function inorder(node, arr) {
  if (node) {
    inorder(node.left, arr);
    arr.push(node);
    inorder(node.right, arr);
  }
}

let tree = new TreeNode(2);
tree.left = new TreeNode(1);
tree.right = new TreeNode(3);
tree.insert(9);

console.log(tree);
