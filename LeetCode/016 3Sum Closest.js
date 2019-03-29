/*
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/

const threeSumClosest = (nums, target) => {
  let result = Infinity;
  nums.sort((a, b) => a - b, 0);

  for (let i = 0; i < nums.length - 2; i++) {
    let current = nums[i];
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = current + nums[left] + nums[right];
      if (Math.abs(target - sum) < Math.abs(target - result)) result = sum;
      if (sum < target) left++;
      else if (sum > target) right--;
      else return sum;
    }
  }
  return result;
};

console.log(threeSumClosest([-1, 2, 1, -4], 1), 2);
// console.log(threeSumClosest([1, 1, -1, -1, 3], 1));
