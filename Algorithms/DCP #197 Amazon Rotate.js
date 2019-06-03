/* 
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

let array = [1,2,3,4,5]
let k = 2;
=> [4,5,1,2,3];
*/

const rotate = (arr, k) => {
  while (k > 0) {
    arr.unshift(arr.pop());
    k--;
  }
  return arr;
};

console.log(rotate([1, 2, 3, 4, 5], 2));
