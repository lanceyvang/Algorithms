/* 
Consider all the leaves of a binary tree.  From left to right order, 
the values of those leaves form a leaf value sequence.

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
*/

function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

let root1 = new TreeNode(2);
root1.left = new TreeNode(3);
root1.right = new TreeNode(4);
root1.left.left = new TreeNode(5);
root1.left.right = new TreeNode(6);
// 564

let root2 = new TreeNode(2);
root2.left = new TreeNode(5);
root2.right = new TreeNode(3);
root2.right.left = new TreeNode(6);
root2.right.right = new TreeNode(9);
// 564

function leafSimilar(root1, root2) {
  let root1Str = findLeaf(root1);
  let root2Str = findLeaf(root2);

  return root1Str === root2Str;

  function findLeaf(node) {
    let str = '';
    let arr = [node];
    while (arr.length) {
      let removed = arr.shift();

      if (removed.right) arr.unshift(removed.right);
      if (removed.left) arr.unshift(removed.left);
      if (!removed.left && !removed.right) str += removed.val;
    }
    return str;
  }
}

console.log(leafSimilar(root1, root2)); // false;

var leafSimilar = function(root1, root2) {
  let arr1 = [];
  let arr2 = [];
  inOrder(root1, arr1);
  inOrder(root2, arr2);

  if (arr1.length === arr2.length) {
    for (let i = 0; i < arr1.length; i++) {
      if (arr1[i] !== arr2[i]) {
        return false;
      }
    }
    return true;
  }
  return false;
};

function inOrder(node, arr) {
  if (node) {
    inOrder(node.left, arr);
    inOrder(node.right, arr);
    if (!node.left && !node.right) {
      arr.push(node.val);
    }
  }
}
