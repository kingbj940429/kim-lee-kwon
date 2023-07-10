# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        visited = []
        cur_node = head

        while cur_node:
            visited.append(cur_node.val)
            cur_node = cur_node.next

        return True if visited == visited[::-1] else False