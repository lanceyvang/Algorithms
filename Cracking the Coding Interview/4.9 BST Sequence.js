/*
BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each element. 
Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

permutator(['c','a','t']);
Yields...

[ [ 'c', 'a', 't' ],
  [ 'c', 't', 'a' ],
  [ 'a', 'c', 't' ],
  [ 'a', 't', 'c' ],
  [ 't', 'c', 'a' ],
  [ 't', 'a', 'c' ] ]
And...

permutator([1,2,3]);
Yields...

[ [ 1, 2, 3 ],
  [ 1, 3, 2 ],
  [ 2, 1, 3 ],
  [ 2, 3, 1 ],
  [ 3, 1, 2 ],
  [ 3, 2, 1 ] ]
*/

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

let tree = new TreeNode(2);
tree.left = new TreeNode(1);
tree.right = new TreeNode(3);

const bstSequences = root => {
  let arr = [];
  dfs(root);
  return permute(arr).filter(el => el[0] === arr[0]);

  function dfs(node) {
    if (node) {
      arr.push(node.val);
      dfs(node.left);
      dfs(node.right);
    }
  }
};

function permute(array) {
  var length = array.length;
  let result = [array.slice()];
  let c = new Array(length).fill(0);
  let i = 1;
  let k;
  let p;

  while (i < length) {
    if (c[i] < i) {
      k = i % 2 && c[i];
      p = array[i];
      array[i] = array[k];
      array[k] = p;
      ++c[i];
      i = 1;
      result.push(array.slice());
    } else {
      c[i] = 0;
      ++i;
    }
  }
  return result;
}

console.log(bstSequences(tree));
