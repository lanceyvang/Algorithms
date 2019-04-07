/*
First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
Avoid storing additional nodes in a data structure. 
NOTE: This is not necessarily a binary search tree.
*/

const firstCommonAncestor = (root, node1, node2) => {
  return dfs(root);

  function dfs(node) {
    if (node.left === node1 || (node2 && node.right === node1) || node2)
      return node;
    console.log(node.val);
    dfs(node.right);
    dfs(node.left);
  }
};
