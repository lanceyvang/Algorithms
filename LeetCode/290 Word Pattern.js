// const wordPattern = (pattern, str) => {
//   str = str.split(' ');
//   if (pattern.length !== str.length || !pattern.length) return false;
//   let hash = {};
//   let arr = [];

//   for (let i = 0; i < pattern.length; i++) {
//     let patternChar = pattern[i];
//     let strChar = str[i];
//     if (!hash[patternChar] && !arr.includes(strChar)) {
//       hash[patternChar] = strChar;
//       arr.push(strChar);
//     } else {
//       if (hash[patternChar] === strChar) continue;
//       else return false;
//     }
//   }
//   return true;
// };

// const wordPattern = (pattern, str) => {
//   str = str.split(' ');

//   if (str.length !== pattern.length || !pattern.length) return false;

//   let map = new Map(),
//     set = new Set();

//   for (let i = 0; i < str.length; i++) {
//     let strChar = str[i];
//     let patternChar = pattern[i];
//     let result = map.get(patternChar);

//     if (!result) {
//       if (set.has(strChar)) return false;
//       map.set(patternChar, strChar);
//       set.add(strChar);
//     } else {
//       if (result !== strChar) return false;
//     }
//   }
//   return true;
// };

const wordPattern = (pattern, str) => {
  if (!pattern.length) return false;
  str = str.split(' ');
  if (pattern.length !== str.length) return false;
  let patternHash = {};
  let strHash = {};

  for (let i = 0; i < pattern.length; i++) {
    let patternChar = pattern[i];
    let strChar = str[i];
    if (!patternHash[patternChar] && !strHash[strChar]) {
      patternHash[patternChar] = strChar;
      strHash[strChar] = true;
    } else {
      if (patternHash[patternChar] === strChar) continue;
      else return false;
    }
  }

  return true;
};

console.log(wordPattern('aba', 'aa bb aa'));
