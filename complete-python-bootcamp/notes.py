# Python

## String Interpolation
# print('This is a string {}'.format('INSERTED'))
# print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

## Formatting floats '{value:width.precision f}'
# result = 10000/777

# print('The result was {r:1.3f}'.format(r=result))

## F-Strings
# name = 'Jose'
# print(f'Hello, his name is {name}')

# new_list = [4,1,8,3]
# new_list.sort()
# print(new_list)

# Files
# import sys
# myfile = open(sys.argv[1], 'r').read()
# myfile = open('/home/lanceyvang/Interviewing/complete-python-bootcamp/myfile.txt') # if the file is in the same folder, you can just use the name
# print(myfile.read())
# myfile.seek(0)
# print(myfile.readlines())
# Windows: myfile = open("C:\\Users\\UserName\\Folder\\test.txt")
# myfile = open("/Users/YouUserName/Folder/myfile.txt")
# with open('/home/lanceyvang/Interviewing/complete-python-bootcamp/myfile.txt') as my_new_file:
#     contents = my_new_file.read()

# with open('myfile.txt') as my_new_file:
#     contents = my_new_file.read()
    # contents = my_new_file.readlines()

'''
with open('my_new_file.txt', mode='r') as f:
    print(f.read())

with open('my_new_file.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')

with open('asdasdsa.txt', mode='w') as f:
    f.write('I created this file!')

mode='r'
mode='w' # write only, will overwrite files or create new
mode='a'
mode='r+' # reading and writing
mode='w+' # overwrites existing file or creates a new file
'''

# with open('newfile.txt', mode='w+') as content:
#     content.write('Writing inside the new file!')
#     content.seek(0)
#     print(content.read())

# with open('myfile.txt', mode='a') as content:
#     content.write('\nThis is on a new line')
#     content.seek(0)
#     print(content.read())
# answer = None

# print([0]*10)

'''
1 < 2 < 3 
same as 
1 < 2 and 2 < 3
can use parenthesis for greater clarity
(1 < 2) and (2 < 3)

not(1 == 1)
not 1 == 1
'''
# Map
# def square(num):
#     return num**2

# my_nums = [1,2,3,4,5]
# '''
# for item in map(square, my_nums):
#     print(item)
# '''

# x = list(map(square, my_nums))
# # print(x)

# def check_even(num):
#     return num % 2 == 0

# mynums = [1,2,3,4,5,6]

# # y = list(filter(check_even, mynums))

# # Lambdas
# # square = lambda num: num ** 2
# # print(square(5))
# x = list(map(lambda num:num**2,mynums))
# print(x)

# names = ['Andy', 'Eve', 'Sally']
# x = list(map(lambda x:x[::-1],names))
# print(x)

'''
x = 50

def func():
    global x # this is the global keyword, should be careful

    x = 200

same as

def func(x):
    x = 200

x = func(x)
'''
## OOP allows us to create code that is repeatable and organized

class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name,spots):
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots
    
    # OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print(f'WOOF! My name is {self.name} and my favorite number is {number}!')

my_dog = Dog(breed='Lab',name='Sammy',spots=False)
# print(my_dog.bark(7))

class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi # radius * radius * Circle.pi
    
    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
    
# my_circle = Circle(30)
# print(my_circle.radius)
# print(my_circle.get_circumference())

class Animal():
    def __init__(self):
        print('ANIMAL CREATED')
    
    def who_am_i(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating')

# my_animal = Animal()
# my_animal.eat()

# Inheritance
# class Dog(Animal):

#     def __init__(self):
#         Animal.__init__(self)
#         print('Dog Created')
    
#     def who_am_i(self):
#         print('I am a dog!')
    
#     def bark(self):
#         print('WOOF!')

# my_dog = Dog()
# my_dog.eat()
# my_dog.who_am_i()

# Polymorphism
# class Dog():

#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return self.name + ' says woof!'

# class Cat():

#     def __init__(self, name):
#         self.name = name
    
#     def speak(self): 
#         return self.name + ' says meow!'
    
# niko = Dog('niko')
# felix = Cat('felix')

# for pet in [niko,felix]:
#     print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

# pet_speak(niko)

# Abstract Class, never expects to be instantiated!!! What I need to rewrite my script with!
# class Animal():
    
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         raise NotImplementedError('Subclass must implement this abstract method')

#     def eat(self):
#         return 'I am eating!'

# class Dog(Animal):
    
#     def speak(self):
#         return self.name+ ' says woof!'

# class Cat(Animal):
    
#     def speak(self):
#         return self.name+ ' says meow!'

# fido = Dog('Fido')
# isis = Cat('Isis')

# myanimal = Animal('Bird')
# print(myanimal.eat())

# Special Methods and Magic Methods
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self): 
        return f'{self.title} by {self.author}'
    
    def __len__(self): # returns the len of user defined objects
        return self.pages

    def __del__(self):
        print('A book object has been deleted')

# b = Book('Python rocks', 'Jose', 200)
# print(b)
# del b

# from colorama import init
# init()
# from colorama import Fore
# print(Fore.RED + 'some red text')

# from MyMainPackage import some_main_script
# from MyMainPackage.SubPackage import mysubscript

# some_main_script.report_main()
# mysubscript.sub_report()

# When you are importing from a module, you would like to know whether a modules function is being used as an import, or if you are using the original .py file of that module.
# if __name__ == '__main__':
#     pass

# number2 = input('Please provide a number: ')
# print(number2)

# try:
#     # WANT TO ATTEMPT THIS CODE
#     # MAY HAVE AN ERROR
#     result = 10 + '10'
# except:
#     print("Hey, it looks like you aren't adding correctly!")

# try:
#     f = open('testfile','r')
#     f.write('Write a test line')
# except TypeError:
#     print('There was a type error!')
# except OSError:
#     print('Hey you have an OS Error!')
# except: 
#     print('All other exceptions!')
# finally:
#     print('I always run')

def ask_for_int():

    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print('Whoops! That is not a number')
            continue
        else:
            print(f'Yes thank you, your number is {result}')
            break
        # finally:
        #     print('Im going to ask you again')

# ask_for_int()

# for i in ['a', 'b', 'c']:
#     try:
#         print(i**2)
#     except TypeError:
#         print('TypeError!')
#     except:
#         print('Unknown Error!')

# x = 5
# y = 1

# try:
#     x/y
# except:
#     print('There is an error!')
# finally:
#     print('All Done.')

### 81. Decorators with Python Overview
'''
Python has decorators that allow ou to tack on extra functionality to an already existing function.
They use the @ operator and are then placed on the top of the original function.

@some_decorator
def simple_func():
    # Do simple stuff
    return something
'''
def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before he original function')
        original_func()
        print('Some extra code, after the original function!')

    return wrap_func



@new_decorator # Our on or off switch, common in Jango and Flask; 
def func_needs_decorator():
    print('I want to be decorated!!')

# same functionality as @
# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()

# func_needs_decorator()

### 83. Generators with Python # generate values as you need them
# def create_cubes(n):
#     result = []
#     for x in range(10):
#         result.append(x**3)
#     return result

# print(create_cubes(10))

def create_cubes(n):
    for x in range(10):
        yield x**3 # a lot more memory efficient

# for x in create_cubes(10):
#     print(x)

# print(list(create_cubes(10))) if you want the list

# def gen_fibon(n):
#     a = 1
#     b = 1

#     for i in range(n):
#         yield a
#         a,b = b, a+b

# for number in gen_fibon(10):
#     print(number)

# def gen_fibon(n):
#     a = 1
#     b = 1
#     output = []

#     for i in range(n):
#         output.append(a)
#         a,b = b, a+b
#     return output

# print(gen_fibon(11))

def simple_gen():
    for x in range(3):
        yield x

# for num in simple_gen():
#     print(num)

g = simple_gen()

# print(next(g))
# print(next(g))

def gensquares(N):
    for x in range(N):
        yield x**2

# for x in gensquares(10):
#     print(x)

import random

# def rand_num(low, high, n):
#     for x in range(n):
#         yield random.randint(low, high)

# for num in rand_num(1, 10, 10):
#     print(num)

s = 'hello'

s_iter = iter(s)

# print(next(s_iter))
# print(next(s_iter))

my_list = [1,2,3,4,5]

# like list comprehension but gencomp generates it as you need it.
gencomp = (item for item in my_list if item > 3)

# print(list(gencomp))

### 87. Collections Module - counter
from collections import Counter

l = [1,2,3,4,1,2,3,2]

# print(Counter(l))

s = 'How many ties does each word show up in this sentence word word up'
c = Counter(s.split(' '))
# print(c.most_common(2))
# sum(c.values())
# list(c)
# set(c)
# dict(c)
# c.items()
# Counter(dict(list_of_pairs))
# c += Counter() # remove zero and negative counts
# print(c.most_common()[:-2-1:-1]) # n least common elements

from collections import defaultdict

# d = {'k1':1}
# print(d['k2']) # will cause error
# print(d['k1'])

d = defaultdict(object)

d['one']

# for item in d: 
#     print(item)

d = defaultdict(lambda: 0)
# print(d['one'])

d['two'] = 2

# print(d['two'])

### 89.OrderedDict
# from collections import OrderedDict

# d = OrderedDict()

### 90. Collections Modeule Named Tuple
from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2,breed='Lab',name='Sammy')

# print(sam.age)

### 91. Datetime
import datetime

t = datetime.time(5,25,1)
# print(t)
# print(t.hour)

today = datetime.date.today()
# print(today)
# print(today.month)

d1 = datetime.date(2015,3,11)
# print(d1)

d2 = d1.replace(year=1990)
# print(d2)

# print(d1-d2) # gives us time delta

### 92. Python Debugger pdb
import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z 
# print(result)

# pdb.set_trace()

# result2 = y + x
# print(result2)

## 93. Timing your code
'''
How to tell if doing things one way or the other is faster.
'''

import timeit


# # generator comprehension
# print(timeit.timeit("'-'.join(str(n) for n in range(100))", number=999)) 

# # list comprehension
# print(timeit.timeit("'-'.join([str(n) for n in range(100)])", number=999)) 

# # map
# print(timeit.timeit("'-'.join(map(str, range(100)))", number=999)) 

'''
Print out 
0.012254517998371739
0.010661407999577932
0.008556519998819567
'''

x = '-'.join(map(str, range(100)))

# print(x, type(x))

### 94. Regular Expressions -re
import re

patterns = ['term1', 'term2']
text = 'this is  string with term1, but not the other term'

match = re.search(patterns[0], text)
match_idx = match.start()
# print(match)

split_term = '@'
phrase = 'What is your email, is it hello@gmail.com?'
re.split(split_term, phrase)

length = len(re.findall('match', 'Here is one match, here is another match'))

test_phrase = 'This is a string. But it has puctuation.'
no_punctuation = re.findall('[^!.?]+', test_phrase)
# print(no_punctuation)

### 95. StringIO
# import StringIO
# convert string to files

### 97. Advanced Numbers
# hexadecimals
hex(246)
bin(128)
pow(2,4,3)
abs(-3)
round(3.1)
round(3.141592,2)

### 98. Advanced Strings
s = 'hello world'
s.capitalize()
s.upper()
s.lower()
s.count('o')
s.find('o')
s.center(20,'z')
'hello\tthi'.expandtabs()
s.isalnum()
s.isalpha()
s.islower()
s.isspace()
s.istitle()
s.isupper()
s.endswith('o')
s.split('e')
s.partition('i') # similar to split but only does it at the first instance

### 99. Advance Sets
s = set()
s.add(1)
s.add(2)
s.clear()
s = {1,2,3}
sc = s.copy()
s.difference(sc) # finds the difference between two sets
s.intersection(sc) # finds the common of two sets
s.intersection_update(sc) # updates a set with the intersection of two sets

s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2) # removes numbers found in s2 from s1
# print(s1)

s.discard(1)

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

s1.isdisjoint(s3) # True, because they don't have an intersection
s1.issubset(s2)
s2.issuperset(s1)

s1.symmetric_difference(s2) # {4}

s1.union(s2) # {1,2,4}
s1.update(s2) # {1,2,4}

### 100. Advanced Dictionaries
d = {'k1':1, 'k2':2}
{x:x**2 for x in range(10)} # dictionary comphrehension

{k:v**2 for k,v in zip(['a','b'], range(2))} # using zip

# for k in d.items():
#     print(k)

### 101. Advanced List
l = [1,2,3]
l.append(4)
l.count(3)

x = [1,2,3]
x.extend([4,5])

l.index(2)

l.insert(2,'inserted')
l.remove('inserted') # remove first instance
l.reverse() # works in place (side-effect)
l.sort()

### 163. Map
def fahrenheit(T):
    return (9.0/5)*T + 32

temp = [0,22.5,40,100]
# m = map(fahrenheit, temp)
m = map(lambda T: (9/5)*T + 32, temp)
# print(list(m))

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

m2 = map(lambda x,y,z: x+y+z, a,b,c)
# print(list(m2))
a_neg = map(lambda num: num*-1, a)
# print(list(a_neg))

### 164. Reduce
from functools import reduce
num_list = [47,11,42,13]
reduced_list = reduce(lambda x,y: x+y, num_list)
# print(reduced_list)
max_find = reduce(lambda a,b,: a if a > b else b, a)
# print(max_find)

### 166. Filter
f = filter(lambda x: True if x%2 == 0 else False, a)
# print(list(f),a)

### 166. Zip
x = [1,2,3]
y = [4,5,6]
z = zip(x,y)
# print(list(z))
# for pair in zip(a,b):
#     print(max(pair))

m = map(lambda pair: max(pair), zip(a,b,))
# print(list(m))

### 167. Enumerate
l = ['a','b','c']
for count,item in enumerate(l):
    print(count,item)

### 168. all() and any()
l = [True, False, False]
any(l)
all(l)
