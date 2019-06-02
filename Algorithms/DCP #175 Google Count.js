/*
#175 Easy
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
*/

const count_chain = (state, steps, arr) => {
  const hash_table = generate_hash();
  return generate_results();

  function generate_hash() {
    const hash = {};
    for (let i = 0; i < arr.length; i++) {
      const [name, letter, amount] = arr[i];
      if (!hash[name]) hash[name] = '';
      hash[name] += letter.repeat(amount * 1000);
    }
    return hash;
  }

  function generate_results() {
    const hash = {};
    while (steps-- > 0) {
      hash[state] ? hash[state]++ : (hash[state] = 1);
      const index = Math.floor(
        Math.random() * Math.floor(hash_table[state].length)
      );
      state = hash_table[state][index];
    }
    return hash;
  }
};

const probabilities = [
  ['a', 'a', 0.9],
  ['a', 'b', 0.075],
  ['a', 'c', 0.025],
  ['b', 'a', 0.15],
  ['b', 'b', 0.8],
  ['b', 'c', 0.05],
  ['c', 'a', 0.25],
  ['c', 'b', 0.25],
  ['c', 'c', 0.5]
];

console.log(count_chain('a', 5000, probabilities));
