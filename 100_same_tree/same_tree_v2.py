class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traversal(self, node, memo):
        if node is not None:
            memo.append(node.val)
            self.traversal(node.left, memo)
            self.traversal(node.right, memo)
        else:
            memo.append(None)

    def isSameTree(self, p, q):
        p_memo = []
        q_memo = []
        self.traversal(p, p_memo)
        self.traversal(q, q_memo)
        p_n = len(p_memo)
        q_n = len(q_memo)
        if p_n != q_n:
            return False
        else:
            for i in range(p_n):
                if p_memo[i] != q_memo[i]:
                    return False
        return True

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