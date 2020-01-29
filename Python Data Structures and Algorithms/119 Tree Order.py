import collections


class Node:

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(3)


# def levelOrderPrint(tree):

#     if not tree:
#         return

#     nodes = collections.deque([tree])

#     currentCount = 1
#     nextCount = 0

#     while len(nodes) != 0:
#         currentNode = nodes.popleft()
#         currentCount -= 1

#         print(currentNode.val)

#         if currentNode.left:
#             nodes.append(currentNode.left)
#             nextCount += 1

#         if currentNode.right:
#             nodes.append(currentNode.right)
#             nextCount += 1

#         if currentCount == 0:
#             print('\n')
#             currentCount, nextCount = nextCount, currentCount

def levelOrderPrint(tree):

    if not tree:
        return

    nodes = [tree, 'next']
    current_string = ''

    while len(nodes) > 1:
        currentNode = nodes.pop(0)

        if currentNode == 'next':
            print(f'{current_string}\n')
            current_string = ''
            nodes.append('next')
        else:
            current_string += str(currentNode.val) + ' '

            if currentNode.left:
                nodes.append(currentNode.left)

            if currentNode.right:
                nodes.append(currentNode.right)

    print(current_string)


levelOrderPrint(root)
