'''
Given two strings, check to see if they are anagrams.
Ignore spaces and capitalization.
'''
# from collections import Counter


def anagram(s1, s2):
    '''
    Using remove_spaces helper functions
    '''
    # m1 = remove_spaces(s1)
    # m2 = remove_spaces(s2)
    # return sorted(m1) == sorted(m2)
    '''
    Using .replace()
    '''
    # s1 = s1.replace(' ', '').lower()
    # s2 = s2.replace(' ', '').lower()
    # return sorted(s1) == sorted(s2)
    '''
    Using Counter module
    '''
    # s1 = s1.replace(' ','').lower()
    # s2 = s2.replace(' ','').lower()
    # s1 = Counter(s1)

    # for char in s2:
    #     if char in s1:
    #         s1[char] -= 1

    # for k in s1:
    #     if s1[k] != 0:
    #         return False

    # return True
    '''
    Not using Counter module
    '''
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    count = {}

    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in s2:
        if char in count:
            count[char] -= 1

    for key in count:
        if count[key] != 0:
            return False

    return True

# def remove_spaces(s):
#     result = ''
#     for char in s:
#         if char.isalpha():
#             result += char
#     return result

# a = 'clint eastwood'
# b = 'old west action'

# print(anagram(a,b))


'''
Given an integer array, output all unique pairs that sum up to a specific value K.
'''
# def pair_sum(nums,target):
#     nums = sorted(nums)
#     result = []
#     l = 0
#     r = len(nums)-1

#     while l < r:
#         sum = nums[l] + nums[r]
#         if sum == target:
#             result.append((nums[l],nums[r]))
#         if sum < target:
#             l += 1
#         else:
#             r -= 1

#     return result


def pair_sum(nums, target):
    if len(nums) < 2:
        return 'Less than 2 nums.'

    seen = set()
    result = set()

    for num in nums:
        diff = target - num

        if diff not in seen:
            seen.add(num)
        else:
            mini = min(num, diff)
            maxi = max(num, diff)
            result.add((mini, maxi))

    return list(result)
    # print('\n'.join(map(str,list(result))))

# print(pair_sum([1,3,2,2,2],4))


'''
Find which element is missing in the second array.
'''


def finder(a1, a2):
    # return list(set(a1).difference(a2))
    result = []

    for num in a1:
        if num not in a2:
            result.append(num)

    # for num1,num2 in zip(arr1,arr2):
    #     if num1 != num2:
    #         return num1

    return result


'''
Find the largest continuous sum
'''


def large_cont_sum(arr):
    max_sum = 0
    curr_sum = 0
    # max_sum = curr_sum = 0

    for num in arr:
        curr_sum = max(curr_sum + num, num)  # creates left boundry
        max_sum = max(max_sum, curr_sum)  # creates right boundry

    return max_sum

# print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))


'''
Given a string of words, reverse all the words. Remove all the leading and trailing whitespace
'''


def rev_words(s):
    # arr = s.split(' ')
    result = ''

    for word in s.split(' '):
        if word != '':
            result = ' ' + word + result

    return result.strip()

# def rev_words(s):
#     result = [word for word in s.split(' ') if word != '']
#     result.reverse()
#     return ' '.join(result)

# def rev_words(s):
#     # return ' '.join(reversed(s.split()))
#     return ' '.join(s.split()[::-1])

# print(rev_words('   space before'))
# print(rev_words('Hi John,   are you ready to go?'))


'''
String Compression
'AAAABBBBCCCCCDDEEEE' => 'A4B4C5D2E4'
'''
# from collections import Counter
# def compress(s):
#     # counter_dict = Counter(s)
#     counter_dict = make_dict(s)
#     result = ''

#     for key in counter_dict:
#         result += f'{key}{counter_dict[key]}'

#     return result

# def make_dict(s):

#     counter_dict = {}

#     for letter in s:
#         if letter in counter_dict:
#             counter_dict[letter] += 1
#         else:
#             counter_dict[letter] = 1

#     return counter_dict


def compress(s):
    count = 1
    result = ''

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += f'{s[i-1]}{count}'
            count = 1

    result += f'{s[-1]}{count}'
    return result

# print(compress('AAAABBBBCCCCCDDEEEE'))
# print(compress('AAAaaa'))
# print(compress('CCCCCCCCCC'))


'''
Unique Characters in String
'abcde' => True
'aabcde' => False
'''


def uni_char(s):
    # my_set = set(s)
    # return len(my_set) == len(s)
    seen = {}

    for letter in s:
        if letter in seen:
            return False
        else:
            seen[letter] = 1

    return True

# print(uni_char('abcde'))

# 67. Implementation of Stack

# class Stack(object):

#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self,item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[len(self.items)-1]

#     def size(self):
#         return len(self.items)

# s = Stack()
# print(s.isEmpty())
# s.push(1)
# s.push('two')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.pop())

# 69. Implementation of Queue


class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # self.items.append(item)
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# q = Queue()
# print(q.isEmpty())


# 70. Deque
'''
Double-ended Queue
Order collections of items similar to the queue.
Has two ends, a front and a rear, and the items remain positioned in the collection.
Hybrid linear structure provides all the capabilities of stacks and queues in a single data structure.
'''


class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# 76. Balanced Parentheses Check
'''
Check to see if opening and closing parentheses are balanced.
'([])' => True
'([)]' => False
'''
# def balance_check(s):

#     if len(s) % 2 != 0:
#         return False

#     stack = []
#     opening = set('([{')
#     matches = set([('[',']'),('(',')'),('{','}')])

#     for char in s:
#         if char in opening:
#             stack.append(char)
#         else:
#             if len(stack) == 0:
#                 return False

#             if (stack.pop(), char) not in matches:
#                 return False

#     return len(stack) == 0

# def balance_check(s):
#     if len(s) % 2 != 0:
#         return False

#     stack = []
#     opening = set('{[(')
#     matches = set([('(',')'),('[',']'),('{','}')])
#     # print(matches)

#     for char in s:
#         if char in opening:
#             stack.append(char)
#         else:
#             if (stack[-1],char) in matches:
#                 stack.pop()

#     return len(stack) == 0


def balance_check(s):
    bank = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for char in s:
        if len(bank) > 0 and char in pairs:
            if bank[-1] == pairs[char]:
                bank.pop()
        else:
            bank.append(char)

    return len(bank) == 0

# print(balance_check('([])'))
# print(balance_check('([)]'))

# 798. Implement a Queue Class using 2 Stacks


class Stack(object):

    def __init__(self):
        self.items = []

    def checkEmpty(self):
        return self.items == []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self):
        return self.items.pop()

    def peek(self):
        if self.checkEmpty():
            return 'Nothing in stack.'
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

# s = Stack()
# s.addItem('apple')
# s.addItem('bananas')
# print(s.peek())

# basically can only use push(append) and pop.


class Queue2Stacks(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        # if stack 2 is empty, then fill it.
        if self.stack2 == []:  # if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


'''
Can only use push (append) and pop.
'''


class Stack2Queue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        self.reverse(self.stack1, self.stack2)
        result = self.stack2.pop()
        self.reverse(self.stack2, self.stack1)
        return result

    def reverse(self, stackA, stackB):
        while stackA:
            stackB.append(stackA.pop())

# q = Stack2Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue())
# print(q.stack1)

# class DoubleStack(object):

#     def __init__(self):
#         self.s1 = []
#         self.s2 = []

#     def enqueue(self,element):
#         self.s1.append(element)

#     def dequeue(self):

#         while len(self.s1):
#             self.s2.append(self.s1.pop())

#         result = self.s2.pop()

#         while len(self.s2):
#             self.s1.append(self.s2.pop())

#         return result

# q = DoubleStack()

# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.dequeue()


# 82. Singly Linked Lists
# class Node(object):

#     def __init__(self,value):
#         self.value = value
#         self.nextnode = None

# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.nextnode = b
# b.nextnode = c
# print(a.nextnode.value)

# 84. Doubly Linked List
# class DoublyLinkedListNode(object):

#     def __init__(self,value):

#         self.value = value
#         self.next_node = None
#         self.prev_node = None

# a = DoublyLinkedListNode(1)
# b = DoublyLinkedListNode(2)
# c = DoublyLinkedListNode(3)

# a.next_node = b
# b.prev_node = a

# b.next_node = c
# c.prev_node = b

# 85. Singy Linked List Cycle Check
'''
Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a cycle.
'''

# class Node(object):

#     def __init__(self,value):
#         self.value = value
#         self.nextnode = None


# def cycle_check(linked_list):
#     seen = []

#     while linked_list.nextnode != None:
#         if linked_list in seen:
#             return True
#         seen.append(linked_list)
#         linked_list = linked_list.nextnode

#     return False

# def cycle_check(linked_list):

#     marker1 = linked_list
#     marker2 = linked_list.nextnode

#     while marker2 != None and marker2.nextnode != None:

#         marker1 = marker1.nextnode
#         marker2 = marker2.nextnode.nextnode

#         if marker2 == marker1:
#             return True

#     return False

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)

# a.nextnode = b
# b.nextnode = c
# c.nextnode = d

# print(cycle_check(a))

# 87. Linked List Reversal
'''
Write a function to reverse a Linked List in place. The function will take in the head of the list as a input and return the new head of the list.
'''
# class Node(object):

#     def __init__(self,value):

#         self.value = value
#         self.nextnode = None

# def reverse(head):

#     current = head
#     previous = None
#     nextnode = None

#     while current:

#         nextnode = current.nextnode
#         current.nextnode = previous

#         previous = current
#         current = nextnode

#     return previous


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(head):
    current = head
    nextnode = previous = None

    while current:
        nextnode, current.nextnode = current.nextnode, previous
        previous, current = current, nextnode

    return previous


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c


def print_node(head):
    while head:
        print(head.value)
        head = head.nextnode


x = reverse(a)
# print_node(x)


# 89. Linked List Nth to Last Node
'''
Return the nth to last node in the linked list.
'''


def nth(head, n):
    left = head
    right = head

    while n:
        if not right.nextnode:
            return 'Linked List is not long enough.'
        else:
            right = right.nextnode

        n -= 1

    while right.nextnode:
        right = right.nextnode
        left = left.nextnode

    print(left.value)
    print(right.value)
    return right


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(nth(a, 1))
