def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0: return min(a,b)
    else: return max(a,b)

# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(2,5))

def animal_crackers(text):
    a,b = text.split(' ')
    return a[0] == b[0]

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

def makes_twenty(n1,n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20: return True
    return False

# print(makes_twenty(20,10))
# print(makes_twenty(2,3))

def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:] 

# print(old_macdonald('macdonald'))

def master_yoda(text):
    return ' '.join(reversed(text.split(' ')))

# print(master_yoda('I am home'))


def almost_there(n):
    return 90 <= n <= 110 or 190 <= n <=210

# print(almost_there(90))
# print(almost_there(209))
# print(almost_there(150))


def has_33(nums):
    pass

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))