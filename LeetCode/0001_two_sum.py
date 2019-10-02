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

print(two_sum([2, 7, 11, 15], 9))

'''
 if len(nums) <= 1:
        return False
        
    dict1 = {}
        #sampledict = {7:0, 2:1,-2:2,-6:3}
    for i in range(len(nums)):

        if nums[i] in dict1:
            return dict1[nums[i]] ,i
        else:
            dict1[target-nums[i]] = i
'''
