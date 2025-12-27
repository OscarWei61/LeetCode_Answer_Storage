# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = ListNode(0)
        current_head = new_head

        while list1 and list2:
            if list1.val <= list2.val:
                current_head.next = list1
                list1 = list1.next
                current_head = current_head.next
            else:
                current_head.next = list2
                list2 = list2.next
                current_head = current_head.next
        
        if list1:
            current_head.next = list1
        
        if list2:
            current_head.next = list2

        return new_head.next