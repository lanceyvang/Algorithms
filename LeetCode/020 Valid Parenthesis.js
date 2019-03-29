/* 
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
*/

// RUNTIME: O(N);
const isValid = s => {
  if (!s.length) return true;
  if (s.length % 2 !== 0) return false;

  const array = [];
  s = s.split('');

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (char === '(') array.push(')');
    else if (char === '[') array.push(']');
    else if (char === '{') array.push('}');
    else if (char === array[array.length - 1]) array.pop();
    else return false;
  }
  return array.length === 0;
};

console.log(isValid('[{}]'));
