/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
*/

const flatten = (obj, result = {}, prepend = '') => {
  for (const word in obj) {
    const value = obj[word];
    // if our value is an object then do recursion
    // if not then just add the value to our result object;
    if (typeof value === 'object') {
      // checks to see what we should input as prepend during recursion;
      // first recursion just adds the word to prepend but following recursions need a '.' before the word;
      const str = prepend.length === 0 ? word : `.${word}`;
      flatten(value, result, (prepend += str));
    } else {
      // prepends our str to our word;
      const str = prepend.length === 0 ? word : `${prepend}.${word}`;
      result[str] = obj[word];
    }
  }
  return result;
};

const dictionary = {
  key: 3,
  foo: {
    a: 5,
    bar: {
      baz: 8
    }
  }
};

flatten(dictionary);
