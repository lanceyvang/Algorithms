/*
Validate BST: Implement a function to check if a binary tree is a binary search tree.
*/

const isValidBST = tree => {
  return validateBST(tree, -Infinity, Infinity);

  function validateBST(root, min, max) {
    if (!root) return true;
    if (root.val >= max || root.val <= min) return false;
    return (
      validateBST(root.left, min, root.val) &&
      validateBST(root.right, root.val, max)
    );
  }
};
