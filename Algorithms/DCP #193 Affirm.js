/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Affirm.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars. Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.
*/

const profit = arr => {
  const results = generate_results(arr);
  return find_max_profit(results);

  function generate_results(stock_arr) {
    const profits_arr = [];
    for (let i = 0; i < stock_arr.length - 1; i++) {
      for (let j = i + 1; j < stock_arr.length; j++) {
        const buy = stock_arr[i];
        const sell = stock_arr[j];
        const fee = 2;
        const profit = sell - buy - fee;
        if (profit > 0) profits_arr.push([[i, j], profit]);
      }
    }
    return profits_arr;
  }

  function find_max_profit(profit_arr) {
    let max = -Infinity;
    let sum = 0;
    for (let i = 0; i < profit_arr.length - 1; i++) {
      for (let j = i + 1; j < profit_arr.length; j++) {
        const current = profit_arr[i];
        const next = profit_arr[j];
        if (current[0][1] < next[0][0]) {
          sum += current[1] + next[1];
          if (sum > max) max = sum;
        }
      }
      sum = 0;
    }
    return max;
  }
};

console.log(profit([1, 3, 2, 8, 4, 10]));
