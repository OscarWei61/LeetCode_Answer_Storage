# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        if left == right:
            return head
        
        dummy_node = ListNode(0)
        dummy_node.next = head
        prev_node = dummy_node

        for _ in range(left-1):
            prev_node = prev_node.next
        
        left_node = prev_node.next
        
        for _ in range(right - left):
            nxt = left_node.next
            left_node.next = nxt.next    
            nxt.next = prev_node.next   
            prev_node.next = nxt        
            
        return dummy_node.next