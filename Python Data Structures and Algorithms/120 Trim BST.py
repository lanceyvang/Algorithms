class Node:

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def trimBST(tree, minVal, maxVal):
    if not tree:
        return

    # trims and modify the left side of the tree
    tree.left = trimBST(tree.left, minVal, maxVal)
    # trims and modify the right side of the tree
    tree.right = trimBST(tree.right, minVal, maxVal)

    # if the code gets to this line, there means the val doesn't fit in range and we need to switch the node with one of it's children
    # says our val is less minVal, we want it to be larger for we use the tree.right
    if tree.val < minVal:
        return tree.right

    # problem since our val is greater than our maxval allowed, so we use the left branch hoping it'll be small than max
    if tree.val > maxVal:
        return tree.left

    return tree


tree = Node(5)
tree.left = Node(4)
tree.right = Node(9)

print(trimBST(tree, 1, 11).right.val)
