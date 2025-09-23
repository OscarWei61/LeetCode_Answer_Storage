# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, max_value):
            if not root:
                return 0
            
            if max_value <= root.val:
                good_node = 1
            else:
                good_node = 0

            max_value = max(max_value, root.val)
            return good_node + dfs(root.left, max_value) + dfs(root.right, max_value)

        return dfs(root, root.val)    
