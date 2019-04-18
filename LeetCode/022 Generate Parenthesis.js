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
    // 2,2,''
    if (!left && !right && str.length) arr.push(str);
    if (left) generate(left - 1, right, str + '('); // 1,2, '(' => 0,2,'(('
    if (right > left) generate(left, right - 1, str + ')'); // 0,1,'(()' => 0,0,'(())'
  }
};

console.log(generateParenthesis(2));
