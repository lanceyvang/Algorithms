/*
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
*/

function permute(nums) {
  let result = [];

  function find(curr, rest) {
    if (!rest.length) return result.push(curr);

    for (let i = 0; i < rest.length; i++) {
      find([...curr, rest[i]], [...rest.slice(0, i), ...rest.slice(i + 1)]);
    }
  }

  find([], nums);

  return result;
}

console.log(permute(['C', 'A', 'T']));
