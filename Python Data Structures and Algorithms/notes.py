# print('hello world')
'''
Given two strings, check to see if they are anagrams.
Ignore spaces and capitalization.
'''
from collections import Counter

def anagram(s1,s2):
    '''
    Using remove_spaces helper functions
    '''
    # m1 = remove_spaces(s1)
    # m2 = remove_spaces(s2)
    # return sorted(m1) == sorted(m2)
    '''
    Using .replace()
    '''
    # s1 = s1.replace(' ', '').lower()
    # s2 = s2.replace(' ', '').lower()
    # return sorted(s1) == sorted(s2)
    '''
    Using Counter module
    '''
    # s1 = s1.replace(' ','').lower()
    # s2 = s2.replace(' ','').lower()
    # s1 = Counter(s1)

    # for char in s2:
    #     if char in s1:
    #         s1[char] -= 1
    
    # for k in s1:
    #     if s1[k] != 0:
    #         return False

    # return True
    '''
    Not using Counter module
    '''
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    count = {}

    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in s2:
        if char in count:
            count[char] -= 1
    
    for key in count:
        if count[key] != 0:
            return False
    
    return True

# def remove_spaces(s):
#     result = ''
#     for char in s:
#         if char.isalpha():
#             result += char
#     return result

# a = 'clint eastwood'
# b = 'old west action'

# print(anagram(a,b))
import unittest

# class TestAnagram(unittest.TestCase):

#     def test_case1(self):
#         a = 'god'
#         b = 'dog'
#         result = anagram(a, b)
#         self.assertEqual(result, True)
    
#     def test_case2(self):
#         a = 'clint eastwood'
#         b = 'old west action'
#         self.assertEqual(anagram(a,b), True)

# unittest.main()

class TestArrayPairSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(pair_sum([1,3,2,2],4), [(1,3),(2,2)])

'''
Given an integer array, output all unique pairs that sum up to a specific value K.
'''
# def pair_sum(nums,target):
#     nums = sorted(nums)
#     result = []
#     l = 0
#     r = len(nums)-1

#     while l < r:
#         sum = nums[l] + nums[r]
#         if sum == target:
#             result.append((nums[l],nums[r]))
#         if sum < target:
#             l += 1
#         else:
#             r -= 1

#     return result

def pair_sum(nums,target):
    if len(nums) < 2: 
        return 'Less than 2 nums.'

    seen = set()
    result = set()

    for num in nums:
        diff = target - num

        if diff not in seen:
            seen.add(num)
        else:
            mini = min(num,diff)
            maxi = max(num,diff)
            result.add((mini,maxi))

    return list(result)
    # print('\n'.join(map(str,list(result))))

# print(pair_sum([1,3,2,2,2],4))
# unittest.main()

'''
Find which element is missing in the second array.
'''
def finder(a1,a2):
    # return list(set(a1).difference(a2))
    result = []

    for num in a1:
        if num not in a2:
            result.append(num)
    
    # for num1,num2 in zip(arr1,arr2):
    #     if num1 != num2:
    #         return num1

    return result

'''
Find the largest continuous sum
'''
def large_cont_sum(arr):
    max_sum = 0
    curr_sum = 0
    # max_sum = curr_sum = 0

    for num in arr:
        curr_sum = max(curr_sum + num,num) # creates left boundry
        max_sum = max(max_sum,curr_sum) # creates right boundry

    return max_sum

# print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))