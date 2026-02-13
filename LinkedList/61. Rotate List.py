# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        if not head or not head.next or k == 0:
            return head
        
        n = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            n = n + 1
        
        k = k % n
        if k == 0:
            return head

        old_tail.next = head
        new_tail = head

        for _ in range(n - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
    
        return new_head
