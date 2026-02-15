# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total = 0 

        def get_number(node, previous_count):
            if not node:
                return

            previous_count = previous_count * 10 + node.val
            
            if not node.left and not node.right:
                self.total = self.total + previous_count

            get_number(node.left, previous_count)
            get_number(node.right, previous_count)
        
        get_number(root, 0)
        return self.total