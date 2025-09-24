# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0

        def dfs(currentSum, root):
            count = 0
            if not root:
                return 0

            if currentSum == root.val:
                count = count + 1
            currentSum = currentSum - root.val

            count = count + dfs(currentSum, root.left) + dfs(currentSum, root.right)
            return count
        
        return dfs(targetSum, root) +  self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)