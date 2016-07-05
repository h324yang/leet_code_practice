class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = True

    def bi_traversal(self, p, q):
        if (p is not None) and (q is not None):
            if p.val == q.val:
                self.bi_traversal(p.left, q.left)
                self.bi_traversal(p.right, q.right)
            else:
                self.res = False
        elif (p is None) ^ (q is None):
            self.res = False
        else:
            pass

    def isSameTree(self, p, q):
        self.bi_traversal(p, q)
        return self.res

if __name__ == "__main__":
    root1 = TreeNode(0)
    root1.left = TreeNode(1)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(6)

    root2 = TreeNode(0)
    root2.left = TreeNode(1)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(6)

    print(Solution().isSameTree(root1, root2))