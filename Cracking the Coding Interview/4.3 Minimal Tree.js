// Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
// write an algo- rithm to create a binary search tree with minimal height.
// Hints: #19, #73, #176

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const minimalTree = arr => {
  if (!arr.length) return null;
  const middle = Math.floor(arr.length / 2);
  const left = arr.slice(0, middle);
  const right = arr.slice(middle + 1);

  const root = new Node(arr[middle]);
  root.left = minimalTree(left);
  root.right = minimalTree(right);

  return root;
};
minimalTree([-10, -3, 0, 2, 5]);
