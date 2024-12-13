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
        merged_node = dummy_node 

        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                merged_node.next = list1
                list1 = list1.next
            else:
                merged_node.next = list2
                list2 = list2.next
            merged_node = merged_node.next

        
        if list1 is not None:
            merged_node.next = list1
        else:
            merged_node.next = list2

        
        return dummy_node.next
