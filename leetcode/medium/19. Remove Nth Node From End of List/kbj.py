# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_cnt = 0
        cur_node = head

        while cur_node:
            node_cnt += 1
            cur_node = cur_node.next

        n = node_cnt - n - 1
        node_cnt = 0

        if n == -1:
            return head.next

        cur_node = head
        while cur_node:
            if node_cnt == n:
                cur_node.next = cur_node.next.next
                break

            node_cnt += 1
            cur_node = cur_node.next

        return head


