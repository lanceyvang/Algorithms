/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].
*/

const largest_subset = arr => {
  let results = [];
  let temp = [];

  for (let i = arr.length - 1; i > 0; i--) {
    for (let j = i - 1; j >= 0; j--) {
      const right = arr[i];
      const left = arr[j];
      if (temp.length === 0) temp.unshift(right);
      if (right % left === 0) temp.unshift(left);
    }
    if (temp.length > results.length) results = temp;
    temp = [];
  }
  return results;
};

console.log(largest_subset([3, 5, 10, 20, 21]));
console.log(largest_subset([1, 3, 6, 24]));
