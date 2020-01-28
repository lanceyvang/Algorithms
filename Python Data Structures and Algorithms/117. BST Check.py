# class Node:
#     def __init__(self, k, val):
#         self.key = k
#         self.value = val
#         self.left = None
#         self.right = None


# def tree_max(node):
#     if not node:
#         return float('-inf')
#     maxleft = tree_max(node.left)
#     maxright = tree_max(node.right)
#     return max(node.key, maxleft, maxright)


# def tree_min(node):
#     if not node:
#         return float('inf')
#     minleft = tree_min(node.left)
#     minright = tree_min(node.right)
#     return min(node.key, minleft, minright)


# def verify(node):
#     if not node:
#         return True
#     if (tree_max(node.left) <= node.key <= tree_min(node.right) and verify(node.left) and verify(node.right)):
#         return True

#     else:
#         return False


# root = Node(10, 'Hello')
# root.left = Node(5, 'Five')
# root.right = Node(30, 'Thirty')
# print(verify(root))

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def verify(node):
    # Base Case
    if not node:
        return True

    # Recursive Case
    if (max_tree_val(node.left) <= node.val <= min_tree_val(node.right)) and verify(node.left) and verify(node.right):
        return True

    return False


def max_tree_val(node):

    if not node:
        return float('-inf')

    return max(node.val, max_tree_val(node.left), max_tree_val(node.right))


def min_tree_val(node):

    if not node:
        return float('inf')

    return min(node.val, min_tree_val(node.left), min_tree_val(node.right))


root = Node(3)
root.left = Node(2)
root.right = Node(1)

print(verify(root))
