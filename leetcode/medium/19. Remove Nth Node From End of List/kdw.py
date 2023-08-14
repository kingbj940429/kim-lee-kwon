# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = target = head
        for _ in range(n):
            tail = tail.next

        if not tail:
            return head.next

        while tail.next:
            tail = tail.next
            target = target.next
        target.next = target.next.next
        return head
