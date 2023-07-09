package leetcode.easy;

import java.util.ArrayDeque;

public class Ljo {

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

    public boolean isPalindrome(ListNode head) {
        var deque = new ArrayDeque<Integer>();
        while(head != null) {
            deque.add(head.val);
            head = head.next;
        }
        while(deque.size() > 3) {
            if(deque.pollFirst().intValue() != deque.pollLast().intValue()) {
                return false;
            }
        }
        return true;

    }

}

