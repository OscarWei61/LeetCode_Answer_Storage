# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow_head = head
        fast_head = head
        while fast_head and fast_head.next:
            slow_head = slow_head.next
            fast_head = fast_head.next.next

        prev = None
        while slow_head:
            next_node = slow_head.next
            slow_head.next = prev
            prev = slow_head
            slow_head = next_node            

        max_value = 0
        first_head = head
        second_head= prev
        while second_head:
            max_value = max(max_value, second_head.val + first_head.val)
            first_head = first_head.next
            second_head = second_head.next
        
        return max_value