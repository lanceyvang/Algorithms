/*
643. Maximum Average Subarray I
Given an array consisting of n integers, find the contiguous subarray 
of given length k that has the maximum average value. And you need to 
output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
*/
function findMaxAverage(arr, k) {
  let max = -Infinity;
  let left = 0;
  let right = k - 1;

  let sum = arr.slice(left, right + 1).reduce((a, b) => a + b, 0);

  while (right < arr.length) {
    let average = sum / k;
    if (average > max) max = average;
    sum -= arr[left++];
    right++;
    sum += arr[right];
  }
  return max;
}

console.log(findMaxAverage([1, 12, -5, -6, 50, 3], 4));
