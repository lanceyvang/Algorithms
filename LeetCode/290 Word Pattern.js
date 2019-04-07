const wordPattern = (pattern, str) => {
  str = str.split(' ');
  if (pattern.length !== str.length) return false;
  let hash = {};
  let arr = [];

  for (let i = 0; i < pattern.length; i++) {
    if (!hash[pattern[i]] && !arr.includes(str[i])) {
      hash[pattern[i]] = str[i];
      arr.push(str[i]);
    } else {
      if (hash[pattern[i]] === str[i]) continue;
      else return false;
    }
  }
  return true;
};

console.log(wordPattern('aaa', 'aa aa aa'));
