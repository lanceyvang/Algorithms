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
//   if (s.length <= 1) return true;
//   s = s.replace(/\W/gi, '').toLowerCase();
//   return (
//     s ===
//     s
//       .split('')
//       .reverse()
//       .join('')
//   );
// };

// const isPalindrome = s => {
//   s = s.replace(/\W/gi, '').toLowerCase();
//   let reversed = '';
//   for (let char of s) {
//     reversed = char + reversed;
//   }
//   return s === reversed;
// };

// const isPalindrome = s => {
//   if (s.length <= 1) return true;
//   s = s.replace(/\W/gi, '').toLowerCase();

//   let center = Math.floor(s.length / 2);
//   let left = s.length % 2 === 0 ? center - 1 : center;
//   let right = center;

//   while (left >= 0 && right <= s.length - 1) {
//     if (s[left] !== s[right]) return false;
//     left--;
//     right++;
//   }
//   return true;
// };

const isPalindrome = s => {
  if (s.length <= 1) return true;
  s = s.replace(/\W/gi, '').toLowerCase();

  let center = Math.floor(s.length / 2);
  let left = s.length % 2 === 0 ? center - 1 : center;
  let right = center;

  for (; right < s.length; right++, left--) {
    if (s[left] !== s[right]) return false;
  }
  return true;
};

console.log(isPalindrome(''));
