# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic = defaultdict(int)

        while headA:
            if headA not in dic:
                dic[headA] = 1

            headA = headA.next

        while headB:
            if headB in dic:
                return headB

            headB = headB.next

        return None