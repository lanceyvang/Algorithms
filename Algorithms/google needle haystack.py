'''
Had a phone interview with Google. The question asked was given below. Just asking Leetcode community the good optimal solution for this.

Suppose you have an array of strings 'src' and a string 'key':

src = {"minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"}
key = "craft"
Now return all the strings from the 'src' array that contains the key as substring in them. For example, for above case, the solution should be:

result = {"minecraftgame", innercrafttalent", "stonecrafter"}
Because all the result starings have key i.e. "craft" in them as substring
'''

# def substring(src, key):
#     # new_arr = []
#     # for word in src:
#     #     if key in word:
#     #         new_arr.append(word)Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# print(substring(["minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"], 'craft'))    
#     # return new_arr
#     return [name for name in src if key in name]
                
'''
Implement int sqrt(int x).

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''
# #import math

# def sqrt_num(x) -> int:
#     #return(int(math.sqrt(x)))
#     return (int(x**.5))
# print(sqrt_num(8))





'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
'''
4
1. 1+1+1+1
2. 2+2
3. 1+2+1
4. 2+1+1
5. 1+1+2
'''

# def climb(n):
#     if n == 1: return 1
#     #if n == 2 :return 2

#     steps = [1, 2]

#     for i in range(2, n):
#         temp = steps[0]
#         steps[0] = steps[1]
#         steps[1] = temp + steps[1]

#     print(steps)
#     return steps[1]

# print(climb(1))


'''
This problem was asked by Jane Street.

The United States uses the imperial system of weights and measures, which means that there are many different, seemingly arbitrary units to measure distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.

Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. You should also allow for additional units to be added to the system.

situation, task, action, result

https://www.w3schools.com/python/python_classes.asp
'''

# class Convert:
#     def __init__(self):
#         pass
#     def converting(fr, to, unit_fr, unit_to):
        
#         pass
#     def inches_to_feet():
#         inches = 24
#         return inches / 12
        
#     def adding():

#         pass

# myconvert = Convert().inches_to_feet(24)
# print(myconvert)


'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

# def rotate(array, k):
#     # for i in range(0, k):
#     #     array.insert(0, array.pop())
#     # return array
#     #ori_len = len(array)
#     k %= len(array)
#     # start = len(array) - k
#     # array = [*array, *array][start : start  +ori_len]
#     array = array[-k:]+array[:-k]
#     return array
    
# print(rotate([1,2,3,4,5,6,7], 3))

'''
136. Single Number
Easy

2917

111

Favorite

Share
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
[1,1,2,2,4]
[1,1,2,2,3,4,4]
Output: 4
'''

# def compare(array):
#     array = sorted(array)
#     while (array[0] == array[1]):
#         array.pop(0)
#         array.pop(0)
#     return array[0]

# print(compare([1,1,2,2,3,4,4]))


'''
This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
'''

# def time(string):
#     hour = int(string.split(":")[0])
#     mins = int(string.split(":")[1])
#     if hour == 12:
#         hour = 0
#     hour_degrees = hour*30
#     mins_degrees = mins*6

#     # 2 mins = 1 degrees (decr if mins are bigger, incr if they are smaller)
#     if hour_degrees > mins_degrees:
#         return hour_degrees - mins_degrees + mins/2
#     else:
#         return mins_degrees - hour_degrees - mins/2
    

# print(time('9:30'))

'''
This problem was asked by Sumo Logic.

Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.
'''
# import math

# def peak(array):
#     if (len(array) == 1): 
#         return array[0]
#     mid = math.floor(len(array) / 2)
#     return max(peak(array[0: mid]), peak(array[mid:]))

# print(peak([0,2,3,4,9,1]))
