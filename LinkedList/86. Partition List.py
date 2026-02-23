# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        small_dummay = ListNode(0)
        big_dummay = ListNode(0)

        small_tail = small_dummay
        big_tail = big_dummay

        current_node = head

        while current_node:
            if current_node.val < x:
                small_tail.next = current_node
                small_tail = small_tail.next
            else:
                big_tail.next = current_node
                big_tail = big_tail.next
        
            current_node = current_node.next
            
        big_tail.next = None

        small_tail.next = big_dummay.next

        return small_dummay.next




            