/*
875. Koko Eating Bananas

Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.
The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, 
and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, 
and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.
Example 1:
Input: piles = [3,6,9,11], H = 8
Output: 5       1,2,2,3=> 8 bananas / H

Example 2:
Input: piles = [30,11,23,4,20], H = 5 // 1, 1, 1, 1, 1 => 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], H = 6 // why can't we just pick second largest #? 
                2, 1, 1, 1, 1 => 30/2 + 11 + 23 + 4 + 20 / 5 => 23?
Output: 23
 
Note:
piles.length <= H
*/
function minEatingSpeed(piles, H) {
  if (H === piles.length) return Math.max(...piles);
}
console.log(minEatingSpeed([30, 11, 23, 4, 20], 6));
