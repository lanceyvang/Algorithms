/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
*/

// const nextPermutation = nums => {

//   let i = findFirstDecreasingElement();

//   if (i < 0) {
//     reverse(0);
//     return nums;
//   } else {
//     let j = findFirstIncreasingElement();
//     swap(i, j);
//     reverse(i + 1);
//   }
//   return nums;

//   // helper functions
//   function swap(a, b) {
//     [nums[a], nums[b]] = [nums[b], nums[a]];
//   }

//   function reverse(start) {
//     let end = nums.length - 1;
//     while (start < end) {
//       swap(start, end);
//       start++;
//       end--;
//     }
//   }

//   function findFirstDecreasingElement() {
//     let i = nums.length - 2;
//     while (i >= 0 && nums[i] >= nums[i + 1]) i--;
//     return i;
//   }

//   function findFirstIncreasingElement() {
//     let j = nums.length - 1;
//     while (j >= 0 && nums[j] <= nums[i]) j--;
//     return j;
//   }
// };

const nextPermutation = nums => {
  let i = nums.length - 2;
  while (i >= 0 && nums[i + 1] <= nums[i]) i--;
  if (i < 0) {
    reverse(0);
    return;
  }

  let j = nums.length - 1;
  while (j >= 0 && nums[j] <= nums[i]) j--;

  swap(i, j);
  reverse(i + 1);

  return nums;

  function swap(a, b) {
    [nums[a], nums[b]] = [nums[b], nums[a]];
  }

  function reverse(start) {
    let end = nums.length - 1;
    while (start < end) {
      swap(start, end);
      start++;
      end--;
    }
  }
};
