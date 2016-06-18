class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def print_tree(self):
        stack = [self]
        while (bool(stack)):
            curr = stack.pop(0)
            print(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)

class Solution(object):
    def exchangeChildren(self, root):
        tmp = root.left
        root.left = root.right
        root.right = tmp

    def invertTree(self, root):
        if root is not None:
            self.exchangeChildren(root)
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root




