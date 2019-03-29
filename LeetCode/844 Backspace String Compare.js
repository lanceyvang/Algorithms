/*
Given two strings S and T, return if they are equal when both 
are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
*/

const hashDelete = (S, T) => {
  if (S.length === 0 && T.length === 0) return true;
  S = process(S);
  T = process(T);

  return S === T;

  // helper function process a string;
  function process(s) {
    const arr = [];

    for (let i = 0; i < s.length; i++) {
      const char = s[i];
      if (char === '#') arr.pop();
      else arr.push(char);
    }
    return arr.join('');
  }
};

console.log(hashDelete('a##c', '#a#c'));
