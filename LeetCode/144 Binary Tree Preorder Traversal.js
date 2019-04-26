/*
144. Binary Tree Preorder Traversal
Favorite

Share
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
*/

/*
144. Binary Tree Preorder Traversal
Favorite

Share
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
*/
function TreeNode(val) {
  this.val = val;
  this.left = null;
  this.right = null;
}

let tree = new TreeNode(1);
tree.left = new TreeNode(2);
tree.left.right = new TreeNode(4);
tree.right = new TreeNode(3);
tree.right.right = new TreeNode(5);

const recursive = root => {
  let arr = [];
  helper(root);
  return arr;

  function helper(root) {
    if (root) {
      arr.push(root.val);
      helper(root.left);
      helper(root.right);
    }
  }
};

const iterative = root => {
  if (!root) return [];
  let arr = [root];
  let results = [];

  while (arr.length) {
    let removed = arr.pop();
    if (removed.val) results.push(removed.val);
    if (removed.right) arr.push(removed.right);
    if (removed.left) arr.push(removed.left);
  }

  return results;
};

console.log(iterative({}));
