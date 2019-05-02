/*
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
*/

const example = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'];

const RPN = arr => {
  let stack = [];

  for (let char of arr) {
    if (typeof char === 'number') {
      stack.push(char);
    } else {
      let right = stack.pop();
      let left = stack.pop();
      let sum = eval(`${left} ${char} ${right}`);
      stack.push(sum);
    }
  }
  return stack[0];
};

console.log(RPN(example));
