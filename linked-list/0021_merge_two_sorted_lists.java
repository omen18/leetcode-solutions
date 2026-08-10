/*
 * Problem: Merge Two Sorted Lists
 * LeetCode #: 21
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/merge-two-sorted-lists/
 *
 * Approach: Dummy node pointer comparison.
 * Time Complexity: O(n + m)
 * Space Complexity: O(1)
 */

public class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        tail.next = (list1 != null) ? list1 : list2;
        return dummy.next;
    }
}
