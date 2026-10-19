# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1

        left = list1
        right = list2
        if left.val <= right.val:
            merged = ListNode(left.val)
            left = left.next
        else:
            merged = ListNode(right.val)
            right = right.next
        
        head = merged
        while left is not None and right is not None:
            if left.val < right.val:
                merged.next = left
                merged = merged.next
                left = left.next
            else:
                merged.next = right
                merged = merged.next
                right = right.next
        
        if left is not None and right is None:
            merged.next = left
        else:
            merged.next = right
        
        return head
            
