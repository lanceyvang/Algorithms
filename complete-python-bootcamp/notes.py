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

my_dict = {'key1':'value1','key2':'value2','key3':3}

for element in my_dict.keys():
    if type(my_dict[element]) == int:
        print('pokemon')
        del my_dict[element]

print(my_dict)