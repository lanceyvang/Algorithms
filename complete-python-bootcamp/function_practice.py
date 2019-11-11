# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0: return min(a,b)
    else: return max(a,b)

# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(2,5))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    a,b = text.split(' ')
    return a[0] == b[0]

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20

# print(makes_twenty(20,10))
# print(makes_twenty(2,3))

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# def old_macdonald(name):
#     return name[0].upper() + name[1:3] + name[3].upper() + name[4:] 

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'

# print(old_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    return ' '.join(text.split(' ')[::-1])

# print(master_yoda('I am home'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return 90 <= n <= 110 or 190 <= n <=210

# print(almost_there(90))
# print(almost_there(209))
# print(almost_there(150))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(1,len(nums)):
        # if nums[i - 1] == 3 and nums[i] == 3: return True
        if nums[i - 1] == 3 == nums[i]: return True

    return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

# print(paper_doll('Hello'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST
def blackjack(*args):
    total = sum(args)

    if total > 21 and 11 in args:
        total -= 10
        return total
    elif total > 21: return 'BUST'
    else: return total


# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    total = 0

    for num in arr:
        if num < 6 or num > 9: total += num

    return total

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order.
def spy_game(nums):
    count = 0

    for num in nums:
        if num == 7 and count == 0: return False
        if num == 0 or num == 7: count += 1
        if count == 3: return True

    return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def is_prime(n):
    for x in range(2, n):
        if n % x == 0: return False 
    return True

def count_primes(num):
    count = 0 
    for n in range(2, num + 1):
        if is_prime(n): count += 1
    
    return count

print(count_primes(100))

# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def print_big(letter):
    pass