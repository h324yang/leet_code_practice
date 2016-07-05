class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.memo = []
        self.check = True

    def traversal_memo(self, node):
        if node is not None:
            self.memo.append(node.val)
            self.traversal_memo(node.left)
            self.traversal_memo(node.right)
        else:
            self.memo.append(None)

    def traversal_check(self, node):
        if not self.memo:
            if node is not None:
                self.check = False
        else:
            tmp = self.memo.pop(0)
            if node is not None:
                if tmp != node.val:
                    self.check = False
                self.traversal_check(node.left)
                self.traversal_check(node.right)
            else:
                if tmp is not None:
                    self.check = False

    def isSameTree(self, p, q):
        self.traversal_memo(p)
        self.traversal_check(q)
        return self.check

if __name__ == "__main__":
    # root1 = TreeNode(0)
    # root1.left = TreeNode(1)
    # root1.right = TreeNode(2)
    # root1.left.left = TreeNode(3)
    # root1.left.right = TreeNode(4)
    # root1.right.left = TreeNode(5)
    # root1.right.right = TreeNode(6)
    #
    # root2 = TreeNode(0)
    # root2.left = TreeNode(1)
    # root2.right = TreeNode(2)
    # root2.left.left = TreeNode(3)
    # root2.left.right = TreeNode(4)
    # root2.right.left = TreeNode(5)
    # root2.right.right = TreeNode(6)
    #
    # print(Solution().isSameTree(root1, root2))