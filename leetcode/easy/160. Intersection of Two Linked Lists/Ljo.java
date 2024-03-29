package leetcode.easy;

import java.util.HashSet;
import java.util.Set;

public class Ljo {

    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode intersection = null;
        Set<ListNode> history = new HashSet<>();
        ListNode pointerA = headA;
        while(pointerA != null) {
            history.add(pointerA);
            pointerA = pointerA.next;
        }
        ListNode pointerB = headB;
        while (pointerB != null) {
            if(history.contains(pointerB)) {
                intersection = pointerB;
                break;
            }
            pointerB = pointerB.next;
        }
        return intersection;
    }

    // https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/49785/java-solution-without-knowing-the-difference-in-len/
//    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
//        //boundary check
//        if(headA == null || headB == null) return null;
//
//        ListNode a = headA;
//        ListNode b = headB;
//
//        //if a & b have different len, then we will stop the loop after second iteration
//        while( a != b){
//            //for the end of first iteration, we just reset the pointer to the head of another linkedlist
//            a = a == null? headB : a.next;
//            b = b == null? headA : b.next;
//        }
//
//        return a;
//    }

}
