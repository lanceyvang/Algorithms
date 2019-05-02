/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
*/

const smallerElement = arr => {
  let results = [];
  for (let i = 0; i < arr.length; i++) {
    let counter = 0;
    for (let j = i + 1; j < arr.length; j++) {
      console.log(arr[j]);
      if (arr[i] > arr[j]) counter++;
    }
    results.push(counter);
  }
  return results;
};

smallerElement([3, 4, 9, 6, 1]);
