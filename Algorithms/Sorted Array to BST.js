class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const sortedArrayToBST = arr => {
  if (!arr.length) return null;
  const middle = Math.floor(arr.length / 2);
  const left = arr.slice(0, middle);
  const right = arr.slice(middle + 1);

  const root = new Node(arr[middle]);
  root.left = sortedArrayToBST(left);
  root.right = sortedArrayToBST(right);
  return root;
};

console.log(sortedArrayToBST([-10, -3, 0, 2, 5]));
