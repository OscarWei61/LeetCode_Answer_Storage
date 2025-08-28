# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev_head = None
        current_head = head 

        while current_head is not None:
            
            next_head = current_head.next
            current_head.next = prev_head
            prev_head = current_head
            current_head = next_head
        
        return prev_head


