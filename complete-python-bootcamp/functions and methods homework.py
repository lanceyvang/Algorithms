import math 

def vol(rad):
    return (4/3) * math.pi * rad**3

# print(vol(5))
    
def ran_check(num,low,high):
    return low <= num <= high

# print(ran_check(5, 6, 10))

def up_low(s):
    up = 0
    low = 0

    for char in s:
        val = ord(char)
        if 65 <= val <= 90: # same as val <= 65 and val <= 90
            up += 1
        elif 97 <= val <= 122:
            low += 1

    print(f'No. of Upper case characters : {up}')
    print(f'No. of Lower case Characters : {low}')

sample = 'Hello Mr. Rogers, how are you this fine Tuesday?'

# up_low(sample)

def unique_list(l):
    return list(set(l))

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def multiply(nums):
    product = 1
    
    for num in nums:
        product *= num

    return product

# print(multiply([1,2,3,-4]))

def palindrome(s):
    # return s == s[::-1]
    reverse = ''

    for char in s:
        reverse = char + reverse
    
    return s == reverse
# print(palindrome('dog'))

import string

def ispanagram(str1, alphabet=string.ascii_lowercase):
    uniques = set(str1.lower())
    return len(uniques) == 27

# print(ispanagram('The quick brown fox jumps over the lazy dog'))


