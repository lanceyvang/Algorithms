/*
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
*/

const climbStairs = n => {
  if (n === 0) return 0;
  if (n === 1) return 1;
  if (n === 2) return 2;

  let arr = [1, 2];

  for (let i = 2; i < n; i++) {
    let temp = arr[0] + arr[1];
    arr[0] = arr[1];
    arr[1] = temp;
    //[arr[0], arr[1]] = [arr[1], arr[0] + arr[1]]
  }
  return arr[1];
};

console.log(climbStairs(9));
