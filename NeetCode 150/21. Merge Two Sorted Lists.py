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
        
        dummy_node = ListNode(0)
        current_node = dummy_node
        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    current_node.next = list2
                    current_node = current_node.next
                    list2 = list2.next
                else:
                    current_node.next = list1
                    current_node = current_node.next
                    list1 = list1.next

            if not list1 and list2:
                while list2:
                    current_node.next = list2
                    current_node = current_node.next

                    list2 = list2.next

            if list1 and not list2:
                while list1:
                    current_node.next = list1
                    current_node = current_node.next
                    list1 = list1.next

            
        return dummy_node.next

