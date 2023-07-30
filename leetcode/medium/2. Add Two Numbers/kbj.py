# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = []
        list_2 = []

        cur_node1 = l1
        cur_node2 = l2

        while cur_node1:
            list_1.append(str(cur_node1.val))
            cur_node1 = cur_node1.next

        while cur_node2:
            list_2.append(str(cur_node2.val))
            cur_node2 = cur_node2.next

        total = list(str(int("".join(list_1[::-1])) + int("".join(list_2[::-1]))))[::-1]

        cur_node = ListNode(val = total[0])
        tmp = cur_node
        for v in total[1:]:
            new_node = ListNode(val = v)
            tmp.next = new_node
            tmp = new_node

        return cur_node