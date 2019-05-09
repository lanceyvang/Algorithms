/*
392. Is Subsequence
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a 
very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (ie, "ace" is a subsequenace of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdca"

Return true.

Example 2: 
s = "axc", t = "ahbgdc"

Return false.
*/

var isSubsequence = function(s, t) {
  let stack = s.split('');

  for (let letter of t) {
    if (letter === stack[0]) stack.shift();
  }

  if (stack.length) return false;
  else return true;
};

var isSubsequence = function(s, t) {
  let beginIndex = 0;
  let haveSameCharInTheRestOfT = false;
  for (let i = 0; i < s.length; i++) {
    haveSameCharInTheRestOfT = false;
    for (let j = beginIndex; j < t.length; j++) {
      if (s[i] === t[j]) {
        haveSameCharInTheRestOfT = true;
        beginIndex = j + 1;
        break;
      }
    }
    if (haveSameCharInTheRestOfT === false) return false;
  }
  return true;
};

console.log(isSubsequence('abca', 'ahbgdca'));
