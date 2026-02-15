# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        current_node = root

        while current_node:
            if current_node.left:
                predecessor = current_node.left
            
                while predecessor.right:
                    predecessor = predecessor.right
                
                predecessor.right = current_node.right

                current_node.right = current_node.left
                current_node.left = None
            
            current_node = current_node.right
        
