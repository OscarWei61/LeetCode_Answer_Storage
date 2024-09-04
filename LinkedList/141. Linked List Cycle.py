# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return False

        slow_node = head
        fast_node = head.next

        while slow_node != fast_node:
            if not slow_node.next or not slow_node:
                return False
            
            if not fast_node or not fast_node.next:
                return False
            
            if slow_node == fast_node:
                return True

            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        return True
        