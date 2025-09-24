# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right

            elif not root.right:
                return root.left
            
            right_successor = self.findMinvalue(root.right)
            root.val = right_successor.val
            root.right = self.deleteNode(root.right, right_successor.val)

        return root

    def findMinvalue(self, node):
        while node.left:
            node = node.left
        
        return node