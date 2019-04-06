/*
Check Balanced: Implement a function to check if a binary tree is balanced. 
For the purposes of this question, 
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
*/

const checkBalanced = root => {
  if (!root) return true;
  let left = getHeight(root.left);
  let right = getHeight(root.right);
  if (Math.abs(left - right) > 1) return false;
  return checkBalanced(root.left) && checkBalanced(root.right);

  function getHeight(node) {
    if (!node) return 0;
    return 1 + Math.max(getHeight(node.left), getHeight(node.right));
  }
};
