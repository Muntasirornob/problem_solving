# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Create a dummy node and initialize a pointer merged_node.
# Compare list1 and list2 values:
# Attach the smaller value to merged_node.next.
# Move the pointer of the selected list and merged_node.
# Attach the remaining nodes of the non-empty list to merged_node.next.
# Return dummy_node.next.


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
