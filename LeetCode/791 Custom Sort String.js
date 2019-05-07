/*
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T 
so that they match the order that S was sorted. More specifically, 
if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "aabbccd" => let newStr => '' + 'cc' + 'bb' + 'aa' 
Output: "cxyzbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

Not

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
*/
function minFallingPathSum(S, T) {
  // iterate through T, create a hash table to keep track of number of times char shows up;
  // creates a hash table;
  // iterate through S now, find out how many repeats a letter has, . repeat;
  let hash = {};

  for (let letter of T) {
    if (!hash[letter]) hash[letter] = 1;
    else hash[letter]++;
  }

  let results = '';

  for (let letter of S) {
    if (hash[letter]) {
      results += letter.repeat(hash[letter]);
      hash[letter] = false;
    }
  }

  for (let letter in hash) {
    if (hash[letter]) results += letter.repeat(hash[letter]);
  }
  return results;
}

console.log(minFallingPathSum('cba', 'abcdabcd')); // ==>'ccbbaadd'
