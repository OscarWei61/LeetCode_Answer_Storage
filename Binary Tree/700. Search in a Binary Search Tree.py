# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def dsf(node):
            if not node:
                return None
            
            if node.val == val:
                return node
        
            left_node = dsf(node.left)

            if left_node:
                return left_node
            
            return dsf(node.right)
        
        return dsf(root)