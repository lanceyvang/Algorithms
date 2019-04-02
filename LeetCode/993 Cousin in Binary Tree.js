/*
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
*/
function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

let newTree = new TreeNode(1);
newTree.left = new TreeNode(2);
newTree.right = new TreeNode(3);
newTree.left.left = new TreeNode(4);
newTree.right.right = new TreeNode(5);

function isSameParent(node, x, y) {
  let arr = [node];

  while (arr.length) {
    let removed = arr.shift();
    if (removed.left && removed.right) {
      let leftVal = removed.left.val;
      let rightVal = removed.right.val;
      if (x === leftVal || (x === rightVal && y === leftVal) || y === rightVal)
        return true;
    }
    if (removed.left) arr.push(removed.left);
    if (removed.right) arr.push(removed.right);
  }
  return false;
}

console.log(isSameParent(newTree, 4, 5));
