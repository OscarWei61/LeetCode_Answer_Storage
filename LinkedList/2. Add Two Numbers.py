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
        new_head = ListNode(0)
        current_head = new_head
        carry = 0

        while l1 or l2 or carry:
            
            if l1:
                num1 = l1.val
            else:
                num1 = 0
            
            if l2:
                num2 = l2.val
            else:
                num2 = 0

            total = num1 + num2 + carry
            current_head.next = ListNode(total % 10)
            current_head = current_head.next 
            carry = total // 10

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        return new_head.next
