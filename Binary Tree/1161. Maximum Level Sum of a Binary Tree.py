# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        sum_level = []

        def dfs(previous_level, node):
            
            if node:
                
                if len(sum_level) < (previous_level + 1):
                    sum_level.append(0)
                
                sum_level[previous_level] = sum_level[previous_level] + node.val

                dfs(previous_level + 1, node.left)
                dfs(previous_level + 1, node.right)

        dfs(0, root)

        return sum_level.index(max(sum_level)) + 1