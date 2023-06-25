# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = defaultdict(int)

        while head:
            if head.next not in dic:
                dic[head.next] = 1
            else:
                return True
            head = head.next

        return False
