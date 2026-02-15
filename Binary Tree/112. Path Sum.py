# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def sum_leaf(node, current_sum):
            if not node:
                return False

            current_sum = current_sum + node.val

            if not node.left and not node.right:
                return current_sum == targetSum
            
            return sum_leaf(node.left, current_sum) or sum_leaf(node.right, current_sum)
        
        return sum_leaf(root, 0)

        return False
