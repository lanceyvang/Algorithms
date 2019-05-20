/*
930. Binary Subarrays With Sum
Medium
In an array A of 0s and 1s, how many non-empty subarrays have sum S?
Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:

      index =>|0, 1, 2, 3, 4
              |
[1,0,1,0,1] =>|1, 0, 1
[1,0,1,0,1] =>|1, 0, 1, 0
[1,0,1,0,1] =>|   0, 1, 0, 1
[1,0,1,0,1] =>|      1, 0, 1
*/

function numSubarraysWithSum(arr, sum) {
  let slow = 0;
  let fast = 1;
  let results = [];

  while (slow < arr.length && fast < arr.length) {
    let newArr = arr.slice(slow, fast + 1);
    let total = newArr.reduce((a, b) => a + b, 0);
    if (total === sum && newArr.length >= 1) {
      results.push(newArr);
      let next = arr[fast + 1];
      if (next === 0) {
        fast++;
      } else {
        slow++;
      }
    } else {
      fast++;
    }
  }
  console.log(results);
  return results.length;
}
//[0,0,0,0,0,0,1,0,0,0]
//0
console.log(numSubarraysWithSum([0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 2));
