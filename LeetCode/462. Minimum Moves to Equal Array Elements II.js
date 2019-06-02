/*
462. Minimum Moves to Equal Array Elements II
Medium
Given a non-empty integer array, find the minimum number 
of moves required 
to make all array elements equal, where a move is 
incrementing a selected 
element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
*/

const minMoves2 = arr => {
  arr = arr.sort((a, b) => a - b);
  const median = arr[Math.floor(arr.length / 2)];
  let counter = 0;

  for (const num of arr) {
    if (num !== median) {
      counter += Math.abs(num - median);
    }
  }
  return counter;
};

console.log(minMoves2([1, 2, 3]));
