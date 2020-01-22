'''
Given a target amount n and a list of distinct coin values, what's the fewest coins needed to make the change amount.
'''
def coin(n,change):
    if n in change:
        return '1 Coin'

    result = []
    change.sort()
    total = 0

    while total < n:
        for val in reversed(change):
            if val + total <= n:
                total += val
                result.append(val)
                break
    print(result)
    return len(result)

print(coin(99,[1,5,25,10]))

'''
const coin = (target,change) => {
  let result = [];
  let total = 0;
  
  if (change.includes(target)) {
    return '1 coin';
  }

  while (total < target) {

    for (let i = change.length-1; i >= 0; i--) {
      let val = change[i];

      if (val + total <= target) {
        result.push(val);
        total += val;
        break;
      }
    }
  }
  console.log(result)
  return `${result.length} Coins`;
};

coin(99,[1,5,10,25]);
'''


# def rec_coin(target,coins):

#     min_coins = target

#     if target in coins:
#         return 1

#     else:
#         for i in [coin for coin in coins if coin<= target]:
#             num_coins = 1 + rec_coin(target-i,coins)

#             if num_coins < min_coins:
#                 min_coins = num_coins
    
#     return min_coins
# print(rec_coin(11,[1,5,10,25]))

# def rec_coin_dynam(target,coins,known_results):

#     min_coins = target

#     if target in coins:
#         known_results[target] = 1
#         return 1
    
#     elif known_results[target] > 0:
#         return known_results[target]

#     else:
#         for i in [c for c in coins if c <= target]:
#             num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)

#             if num_coins < min_coins:
#                 min_coins = num_coins
#                 known_results[target] = min_coins
        
#     print(known_results)
#     return min_coins

# print(rec_coin_dynam(4,[1,5,10],[0]*(4+1)))
