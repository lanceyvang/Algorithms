/*
Give a string s, count the number of non-empty (contiguous) substrings
that have the same number of 0's and 1's, and all the 0's and all the 1's in
these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's:
"0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
696. Count Binary Substrings
var countBinarySubstrings = function (s) { }
*/

const countBinarySubstrings = s => {
  if (s.length <= 1) return 0;
  let previousLength = 0;
  let currentLength = 1;
  let count = 0;

  for (let i = 1; i < s.length; i++) {
    let previous = s[i - 1];
    let current = s[i];
    if (current === previous) {
      currentLength++;
    } else {
      previousLength = currentLength;
      currentLength = 1;
    }
    if (previousLength >= currentLength) {
      count++;
    }
  }
  return count;
};

console.log(countBinarySubstrings('00110011'));

var countBinarySubstrings = function(s) {
  let begin = s[0];
  let counter = 1;
  let result = 0;
  let before = 0;
  let after = 0;

  for (let i = 1; i <= s.length; i++) {
    if (s[i] === begin) counter++;
    else if (s[i] !== begin) {
      begin = s[i];
      after = counter;
      if (before !== 0) result = result + Math.min(after, before);
      before = after;
      counter = 1;
    }
  }
  return result;
};
