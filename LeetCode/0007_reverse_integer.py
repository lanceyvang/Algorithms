'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
def reverse(x: int) -> int:
    
    result: str = ''

    for char in str(x):
        if char != '-': 
            result = char + result

    # sign = [1, -1][x < 0] 
    sign: int = -1 if x < 0 else 1
    result: int = int(result) * sign

    return result if -(2**31)-1 < result < 2**31 else 0

print(reverse(-123))