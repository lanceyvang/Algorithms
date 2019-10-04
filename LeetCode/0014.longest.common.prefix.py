'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

def longestCommonPrefix(strs):

    shortest_word = min(strs, key=len)
    result = ''
    
    for index, char in enumerate(shortest_word):
        for index2, word in enumerate(strs):
            if index2 == len(strs) - 1 and char == word[index]:
                result += char
    
    return result


print(longestCommonPrefix(["flower","flow","flight"]))