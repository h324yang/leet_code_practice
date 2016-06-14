class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            if root.left is None and root.right is None:
                return 1
            else:
                return max(Solution().maxDepth(root.left), Solution().maxDepth(root.right))+1