# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast_point = head
        slow_point = head
        prev_point = None

        if head is None or head.next is None:
            return None

        while fast_point and fast_point.next:
  
            fast_point = fast_point.next.next

            prev_point = slow_point
            slow_point = slow_point.next
        
        prev_point.next = slow_point.next
    
        return head
        
