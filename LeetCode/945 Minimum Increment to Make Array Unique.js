/*
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.



Example 1:

Input: [1,2,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

let hash = {
  '1' : true;
  '2' : true;

}

Input: [3,2,1,2,1,7] => [1,1,2,2,3,7] => [1,2,3,4,5,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
*/

function minIncrementForUnique(A) {
  let set = new Set();
  let counter = 0;

  for (let num of A) {
    if (!set.has(num)) set.add(num);
    else {
      let int = num;
      while (set.has(int)) {
        counter++;
        int += 1;
      }
      set.add(int);
    }
  }
  return counter;
}

var minIncrementForUnique = function(A) {
  let counter = 0;
  A.sort((a, b) => a - b);
  for (let i = 0; i < A.length; i++) {
    if (A[i] === A[i + 1]) {
      A[i + 1] = A[i] + 1;
      counter += 1;
    } else if (A[i] > A[i + 1]) {
      counter += A[i] - A[i + 1] + 1;
      A[i + 1] = A[i] + 1;
    } else continue;
  }
  return counter;
};
console.log(minIncrementForUnique([3, 2, 1, 2, 1, 7]));
