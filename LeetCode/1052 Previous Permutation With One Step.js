console.log('Practice makes Perfect!'); //I cannot see you.
/*
1053. Previous Permutation With One Swap

Given an array A of positive integers (not necessarily distinct), return the lexicographically 
largest permutation that is smaller than A, that can be made with one swap
(A swap exchanges the positions of two numbers A[i] and A[j]).  
If it cannot be done, then return the same array.

Example 1:

Input: [3,2,1] // [3,0,2,1] => [3,0,1,2] 
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: [1,9,4,6,7]  // [1,9,6,4,7] => [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
Example 4:

Input: [3,1,1,3] // 
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.

*/

var prevPermOpt1 = function(A) {
  let right = A.length - 1;
  let left = right - 1;

  while (right > 0) {
    if (A[right] < A[left]) {
      swap(right, left, A);
      return A;
    }
    if (left === 0 && A[left] > A[left + 1]) {
      swap(left, left + 1, A);
      return A;
    }
    if (left > 0) left--;
    else right--;
  }

  return A;

  function swap(a, b, A) {
    [A[a], A[b]] = [A[b], A[a]];
  }
};
console.log(prevPermOpt1([3, 2, 1]));
console.log(prevPermOpt1([1, 1, 5]));
console.log(prevPermOpt1([1, 9, 4, 6, 7]));
console.log(prevPermOpt1([3, 1, 1, 3]));
