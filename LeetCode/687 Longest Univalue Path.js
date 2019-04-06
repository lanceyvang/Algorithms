/*
Given a binary tree, find the length of the longest path where each node in the path has the same value. \
This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
*/

// const longestUnivaluePath = root => {
//   let result = 0;
//   dfs(root);
//   return result;

//   function dfs(root) {
//     if (!root) return 0;
//     let left = dfs(root.left),
//       right = dfs(root.right),
//       maxLeft = 0,
//       maxRight = 0;
//     if (root.left && root.left.val === root.val) maxLeft = left + 1;
//     if (root.right && root.right.val === root.val) maxRight = right + 1;
//     result = Math.max(result, maxLeft + maxRight);
//     return Math.max(maxLeft, maxRight);
//   }
// };

const longestUnivaluePath = root => {
  if (!root) return 0;
  return Math.max(
    longestUnivaluePath(root.left),
    longestUnivaluePath(root.right),
    straightUnivaluePath(root.left, root.val) +
      straightUnivaluePath(root.right, root.val)
  );

  function straightUnivaluePath(node, uniVal) {
    if (!node || node.val !== uniVal) return 0;
    return (
      Math.max(
        straightUnivaluePath(node.left, uniVal),
        straightUnivaluePath(node.right, uniVal)
      ) + 1
    );
  }
};

const longestUnivaluePath = root => {
  if (!root) return 0;
  let maxLength = 0;
  getLength(root, root.val);
  return maxLength;

  function getLength(node, parent) {
    if (!node) return 0;
    let left = getLength(node.left, node.val);
    let right = getLength(node.right, node.val);
    if (left + right > maxLength) maxLength = left + right;
    if (node.val === parent) return 1 + Math.max(left, right);
    return 0;
  }
};
