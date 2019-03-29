/*
1. Two Sum
Easy

10102

325

Favorite

Share
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

// Runtime: O(N)
const twoSum = (nums, target) => {
  const numsMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    const find = target - nums[i];
    if (numsMap.get(find) !== undefined) {
      return [numsMap.get(find), i];
    }
    numsMap.set(nums[i], i);
  }
};

console.log(twoSum([3, 3], 6));
