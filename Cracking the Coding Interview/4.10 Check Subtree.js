/*
Check Subtree: T l and T2 are two very large binary trees, with T l much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree ofT i if there exists a node n in T i such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
*/

const checkSubtree = (T1, T2) => {
  if (T1) {
    if (T2 === T1) return true;
    if (T2.val < T1.val) return checkSubtree(T1.left, T2);
    if (T2.val > T1.val) return checkSubtree(T1.right, T2);
  }
  return false;
};
console.log(checkSubtree(tree1, tree2));
