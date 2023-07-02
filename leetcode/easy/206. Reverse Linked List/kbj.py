# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = []

        if head is None:
            return None

        while head:
            visited.append(head.val)
            head = head.next

        visited = visited[::-1]

        head = ListNode(val=visited[0], next=None)
        tmp = head
        for num in visited[1:]:
            cur = ListNode(val=num, next=None)
            tmp.next = cur
            tmp = cur

        return head