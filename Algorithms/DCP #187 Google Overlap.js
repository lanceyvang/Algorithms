/* 
#187 Easy
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 4)
}
return true as the first and third rectangle overlap each other.
*/

const list = [
  {
    top_left: [1, 4],
    dimensions: [3, 3]
  },
  {
    top_left: [-1, 3],
    dimensions: [2, 1]
  },
  {
    top_left: [0, 5],
    dimensions: [4, 4]
  }
];

const overlap = arr => {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      let current = arr[i];
      let next = arr[i + 1];
      if (
        current.top_left[0] <= next.top_left[0] &&
        current.top_left[1] >= next.top_left[1]
      ) {
        if (
          current.dimensions[0] >= next.dimensions[0] &&
          current.dimensions[1] >= next.dimensions[1]
        )
          return true;
      } else {
        if (
          next.dimensions[0] >= current.dimensions[0] &&
          next.dimensions[1] >= current.dimensions[1]
        )
          return true;
      }
    }
  }
  return false;
};

const overlap = arr => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (helper(arr[i], arr[j])) return true;
    }
  }
  return false;
};

function helper(ret1, ret2) {
  let topLeft1 = ret1.top_left;
  let buttomRight1 = [
    ret1.top_left[0] - ret1.dimensions[0],
    ret1.top_left[1] - ret1.dimensions[1]
  ];
  let topLeft2 = ret2.top_left;
  let buttomRight2 = [
    ret2.top_left[0] - ret2.dimensions[0],
    ret2.top_left[1] - ret2.dimensions[1]
  ];

  if (
    topLeft1[0] >= topLeft2[0] &&
    topLeft1[1] <= topLeft2[1] &&
    buttomRight1[0] >= buttomRight2[0] &&
    buttomRight1[1] <= buttomRight2[1]
  )
    return true;
  return false;
}

console.log(overlap(list));
