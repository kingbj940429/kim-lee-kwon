# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middleNode(head):
            fast = slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverseList(head):
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev

        tail = reverseList(middleNode(head))
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
