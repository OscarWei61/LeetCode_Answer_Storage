# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def getLeaf(root):
            if not root:
                return []
            while root:
                if not root.left and not root.right:
                    return [root.val]
                return getLeaf(root.left) + getLeaf(root.right)
        
        return getLeaf(root1) == getLeaf(root2)