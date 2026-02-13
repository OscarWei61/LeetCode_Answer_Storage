# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        queue = deque([root])
        left_to_right = True
        result = []

        while queue:
            level_length = len(queue)
            level_store = deque()

            for index in range(level_length):
                node = queue.popleft()

                if left_to_right:
                    level_store.append(node.val)
                else:
                    
                    level_store.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if left_to_right:
                left_to_right = False
            else:
                left_to_right = True
            
            result.append(list(level_store))
        
        return result