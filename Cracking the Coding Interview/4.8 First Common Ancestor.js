/*
First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
Avoid storing additional nodes in a data structure. 
NOTE: This is not necessarily a binary search tree.
*/

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

let tree = new TreeNode(6);
tree.left = new TreeNode(2);
let p = new TreeNode(0);
let q = new TreeNode(4);
tree.left.left = p;
tree.left.right = q;
tree.right = new TreeNode(8);

const firstCommonAncestor = (root, p, q) => {
  if (root.val > p.val && root.val > q.val) {
    return firstCommonAncestor(root.left, p, q);
  } else if (root.val < p.val && root.val < q.val) {
    return firstCommonAncestor(root.right, p, q);
  }
  return root;
};

const firstCommonAncestor = (root, p, q) => {
  while (root !== null) {
    if (p.val < root.val && q.val < root.val) {
      root = root.left;
    } else if (p.val > root.val && q.val > root.val) {
      root = root.right;
    } else return root;
  }
  return root;
};
