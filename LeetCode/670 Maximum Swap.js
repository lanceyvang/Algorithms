/*
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.

Example 3:
Input: 9973888
Output: 9983887

Example 4:
Input: 999990999 => 999999099
Output: 999999000 !==

Runtime: 56 ms, faster than 100.00% of JavaScript online submissions for Maximum Swap.
Memory Usage: 33.8 MB, less than 50.00% of JavaScript online submissions for Maximum Swap.
*/

const maximumSwap = num => {
  let num_array = num
    .toString()
    .split('')
    .map(el => +el);
  let max_index = num_array.lastIndexOf(Math.max(...num_array));

  if (num_array[0] !== num_array[max_index]) {
    swap(0, max_index, num_array);
  } else {
    let min_index = num_array.indexOf(Math.min(...num_array));
    let largest_index = num_array.lastIndexOf(
      Math.max(...trim_array(num_array))
    );
    if (largest_index > min_index) swap(largest_index, min_index, num_array);
  }

  return +num_array.join('');

  // HELPER FUNCTIONS
  function swap(i, j, arr) {
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }

  function trim_array(arr) {
    for (let i = 1; i < arr.length; i++) {
      let other_nums = num_array.slice(i);
      if (arr[i] >= Math.max(...other_nums)) continue;
      else return other_nums; // 998017 => 017
    }
    return arr;
  }
};

console.log(maximumSwap(998017));
