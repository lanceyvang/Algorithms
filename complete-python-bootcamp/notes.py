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