'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def two_sum(nums: list, target: int) -> list:

    d: dict = {}
    
    for index, num in enumerate(nums):
        find_num: int = target - num
        if find_num in d: 
            return [d[find_num], index]
        else:
            d[num]: int = index

    return []

print(two_sum([5,75,25], 100))