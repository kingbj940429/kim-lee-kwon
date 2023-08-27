package leetcode.easy;

public class Ljo {

    class ListNode {

        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode dummyHead = new ListNode();
        ListNode prev = dummyHead;
        ListNode current = head;
        while (current != null && current.next != null) {
            prev.next = current.next;
            current.next = prev.next.next;
            prev.next.next = current;

            prev = current;
            current = current.next;
        }
        return dummyHead.next;

    }
}
