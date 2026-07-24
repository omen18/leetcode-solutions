/*
 * Problem: Binary Search
 * LeetCode #: 704
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/binary-search/
 *
 * Approach: Standard binary search with left and right pointers.
 * Time Complexity: O(log n)
 * Space Complexity: O(1)
 */

public class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

    // --- Test ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.search(new int[]{-1, 0, 3, 5, 9, 12}, 9)); // 4
    }
}
