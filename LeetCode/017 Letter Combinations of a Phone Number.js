/* Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, 
your answer could be in any order you want.
*/

// const letterCombinations = digits => {
//   const arr = digits.split('');

//   const hashMap = {
//     '1': [],
//     '2': ['a', 'b', 'c'],
//     '3': ['d', 'e', 'f'],
//     '4': ['g', 'h', 'i'],
//     '5': ['j', 'k', 'l'],
//     '6': ['m', 'n', 'o'],
//     '7': ['p', 'q', 'r'],
//     '8': ['t', 'u', 'v'],
//     '9': ['w', 'x', 'y', 'z']
//   };

//   const a = hashMap[arr[0]];
//   const b = hashMap[arr[1]];

//   const results = [];

//   for (let i = 0; i < a.length; i++) {
//     for (let j = 0; j < b.length; j++) {
//       results.push(a[i] + b[j]);
//     }
//   }
//   return results;
// };

var letterCombinations = function(digits) {
  const mappings = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  };

  if (!digits || digits.length === 0) return [];
  if (digits.length === 1) {
    return mappings[digits];
  }

  let result = [];
  let set1 = letterCombinations(digits.substr(0, 1));
  let set2 = letterCombinations(digits.substr(1));

  for (let i = 0; i < set1.length; i++) {
    for (let j = 0; j < set2.length; j++) {
      result.push(set1[i] + set2[j]);
    }
  }

  return result;
};

console.log(letterCombinations('23'));
