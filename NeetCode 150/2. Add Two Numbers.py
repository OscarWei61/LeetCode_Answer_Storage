# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy_node = ListNode(0)
        current_node = dummy_node
        carry = 0

        while l1 or l2 or carry == 1:
            if not l1:
                lval1 = 0
            else:
                lval1 = l1.val
            
            if not l2:
                lval2 = 0
            else:
                lval2 = l2.val

            if lval2 + lval1 + carry >= 10:
                current_node.next = ListNode(lval2 + lval1 + carry - 10)
                carry = 1
            else:
                current_node.next = ListNode(lval2 + lval1 + carry)
                carry = 0
            
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
            
            current_node = current_node.next

        return dummy_node.next
            

            