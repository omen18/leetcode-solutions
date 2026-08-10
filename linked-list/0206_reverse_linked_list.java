/*
 * Problem: Reverse Linked List
 * LeetCode #: 206
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/reverse-linked-list/
 *
 * Approach: Iterative three-pointer (prev, curr, next) reassignment.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }
}
