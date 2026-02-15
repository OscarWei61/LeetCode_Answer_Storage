"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        current_node = root

        while current_node:

            dummy_node = Node(0)
            temp_node = dummy_node

            while current_node:
                if current_node.left:
                    temp_node.next = current_node.left
                    temp_node = temp_node.next
                
                if current_node.right:
                    temp_node.next = current_node.right
                    temp_node = temp_node.next

                current_node = current_node.next
            
            current_node = dummy_node.next
        
        return root