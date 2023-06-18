package leetcode.easy;

import java.util.HashSet;
import java.util.Set;



public class Ljo {
    static class ListNode {

        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }
        Set<ListNode> checker = new HashSet<>();
        checker.add(head);
        var now = head.next;
        while (true) {
            if (now == null) {
                return false;
            }
            if (checker.contains(now)) {
                return true;
            }
            checker.add(now);
            now = now.next;
        }
    }

//     O(1) memory
//    public boolean hasCycle(ListNode headNode) {
//        ListNode fastPointer = headNode;
//        ListNode slowPointer = headNode;
//        while (fastPointer != null && fastPointer.next != null) {
//            fastPointer = fastPointer.next.next;
//            slowPointer = slowPointer.next;
//            if(slowPointer == fastPointer) {
//                return true;
//            }
//        }
//        return false;
//    }
}
