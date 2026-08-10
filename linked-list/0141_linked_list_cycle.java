/*
 * Problem: Linked List Cycle
 * LeetCode #: 141
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/linked-list-cycle/
 *
 * Approach: Floyd's Tortoise and Hare (slow & fast pointers).
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}
