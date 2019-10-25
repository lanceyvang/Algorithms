'''
You can use copy.deepcopy to make a copy of the original dict, loop over the copy while change the original one.

from copy import deepcopy

d=dict()
for i in range(5):
    d[i]=str(i)

k=deepcopy(d)

d[2]="22"
print(k[2])
#The result will be 2.
Your problem is iterate over something that you are changing.
'''

def remove_string_values_longer_than(n, dic):
    # for k in dic.keys():
        # if len(k)>n:
        #     del dic[k]
    # for k in dic.copy():
    #     if len(k) > n:
    #         del dic[k]

    for k in dic.copy():
        if type(dic[k]) != int and len(k) > n:
            del dic[k]
    
    return dic

input = {'a': 8, 'b': 6, 'c': 'montana', 'age': 'old'}

print(remove_string_values_longer_than(2, input))

