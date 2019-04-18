/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/

const generateParenthesis = n => {
  let arr = [];
  generate(n, n, '');
  return arr;

  function generate(left, right, str) {
    if (!left && !right && str.length) arr.push(str);
    if (left) generate(left - 1, right, str + '(');
    if (right > left) generate(left, right - 1, str + ')');
  }
};

console.log(generateParenthesis(2));
