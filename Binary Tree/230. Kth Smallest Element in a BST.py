# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = []
        current_node = root
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            
            current_node = stack.pop()
            k = k - 1

            if k == 0:
                return current_node.val
            
            current_node = current_node.right
        
            