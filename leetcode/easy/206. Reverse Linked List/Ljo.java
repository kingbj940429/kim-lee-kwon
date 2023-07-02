package leetcode.easy;


class Ljo {

    static class ListNode {

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

    public ListNode reverseList(ListNode head) {
        return recursive(head, null);
    }

    private ListNode recursive(ListNode now, ListNode prev) {
        if (now == null) {
            return prev;
        }
        var next = now.next;
        now.next = prev;
        return recursive(next, now);
    }
}
