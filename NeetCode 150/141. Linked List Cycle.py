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
        
        slow_pointer = head
        fast_pointer = head

        while True:
            
            
            if not slow_pointer or not fast_pointer:
                return False
               
            if slow_pointer.next:
                slow_pointer = slow_pointer.next
            else:
                return False
            if fast_pointer.next and fast_pointer.next.next:
                fast_pointer = fast_pointer.next.next
            else:
                return False
            
            if slow_pointer == fast_pointer:
                break
            
        return True