# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_length = 0

        def dfs(node):
            if not node:
                return (-1, -1)

            left = dfs(node.left)
            right = dfs(node.right)

            self.max_length = max(self.max_length, left[1] + 1, right[0] + 1)

            return (left[1] + 1, right[0] + 1)
        
        dfs(root)

        return self.max_length

