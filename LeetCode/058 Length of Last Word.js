/*
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
*/

// const lengthOfLastWord = s => {
//   if (!s.length || s === ' ') return 0;
//   let arr = s.split(' ')

//   for(let i = arr.length - 1; i >= 0; i--) {
//     if (arr[i].length > 0) return arr[i].length;
//   }
// }

const lengthOfLastWord = s => {
  if (!s) return 0;

  let word = '';
  let left = 0;
  let right = s.length - 1;
  while (right >= left) {
    let letter = s[right];
    if (letter === ' ' && word.length > 0) return word.length;
    if (letter !== ' ') word = word + letter;
    right--;
  }
  return word.length;
};

console.log(lengthOfLastWord('        '));
