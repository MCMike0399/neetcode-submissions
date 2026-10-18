# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        stack: List[ListNode] = []
        curr: ListNode = head

        while curr is not None:
            stack.append(curr)
            curr = curr.next
        
        # by constraints we know n > 1
        head = stack.pop()
        curr = head

        while len(stack) > 0:
            next = stack.pop()
            curr.next = next
            curr = curr.next
        curr.next = None

        return head
