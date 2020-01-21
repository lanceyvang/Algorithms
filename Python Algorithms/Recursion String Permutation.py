def permutation(s):
    result = []
    if len(s) == 0:
        return result
    
    # Base Case
    if len(s) == 1: # if len of 1 then that means you have all the permutations
        return [s]
    
    for i,letter in enumerate(s): # looping through the string to find all the permutations for the current letter
        other_letters = s[:i] + s[i+1:] # create a string of remaining letters to find permutations for
        
        # Recursive
        for perm in permutation(other_letters): # creates a list of all the possible permutations for other_letters 
            result += [letter + perm] # adds each of these possible permutations with the current letter and push it to result variable
    
    return result

print(permutation('abc'))

from itertools import permutations, combinations

x = permutations('123')
print(list(x))

y = combinations('456',2)
print(list(y))

