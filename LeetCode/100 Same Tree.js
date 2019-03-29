/**
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
*/

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = 0;
    this.right = 0;
  }
}

const treeA = new TreeNode(1);
const treeB = new TreeNode(2);

// var isSameTree = function(p, q) {
//   if (!p && !q) return true;
//   if (!p || !q || p.val !== q.val) return false;
//   return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
// };

// const isSameTree = (p, q) => {
//   return JSON.stringify(p) === JSON.stringify(q);
// };

const isSameTree = (p, q) => {
  if (!p && !q) return true;
  if ((!p && q) || (p && !q)) return false;
  let pStr = extract(p);
  let qStr = extract(q);

  return pStr === qStr;

  function extract(node) {
    let arr = [node];
    let str = '';

    while (arr.length) {
      let removed = arr.shift();
      str += removed.val;

      if (removed.left) arr.push(removed.left);
      else str += 'no left';

      if (removed.right) arr.push(removed.right);
      else str += 'no right';
    }
    return str;
  }
};

console.log(isSameTree(treeA, treeB));
