/* 
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/

const threeSum = nums => {
  nums.sort((a, b) => a - b);
  const results = [];

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      if (left > i + 1 && nums[left] === nums[left - 1]) {
        left++;
        continue;
      }
      let sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) results.push([nums[i], nums[left], nums[right]]);
      if (sum > 0) right--;
      else left++;
    }
  }

  return results;
};

let arr = [-1, 0, 1, 2, -1, -4];
console.log(threeSum(arr));
