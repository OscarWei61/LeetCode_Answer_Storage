"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        old_node_to_new = {}

        current_node = head
        while current_node:
            old_node_to_new[current_node] = Node(current_node.val)
            current_node = current_node.next
        
        current_node = head
        while current_node:
            new_node = old_node_to_new[current_node]

            if current_node.next:
                new_node.next = old_node_to_new[current_node.next]
            
            if current_node.random:
                new_node.random = old_node_to_new[current_node.random]
            
            current_node = current_node.next
        
        return old_node_to_new[head]