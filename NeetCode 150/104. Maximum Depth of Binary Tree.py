# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_level = 0

        def dfs(node, level):
            if not node:
                return level
            
            return max(dfs(node.left, level + 1), dfs(node.right, level + 1))

        return dfs(root, 0)