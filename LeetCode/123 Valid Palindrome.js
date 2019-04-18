/* 
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
*/

// const isPalindrome = s => {
//   let filtered = s.replace(/\W/gi, '');
//   return (
//     filtered.toLowerCase() ===
//     filtered
//       .split('')
//       .reverse()
//       .join('')
//       .toLowerCase()
//   );
// };

const isPalindrome = s => {
  s = s.replace(/\W/gi, '');
  let reversed = '';
  for (let char of s) {
    reversed = char + reversed;
  }
  return s.toLowerCase() === reversed.toLowerCase();
};

console.log(isPalindrome('A man, a plan, a canal: Panama'));
