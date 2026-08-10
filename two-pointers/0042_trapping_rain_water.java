/*
 * Problem: Trapping Rain Water
 * LeetCode #: 42
 * Difficulty: Hard
 * Link: https://leetcode.com/problems/trapping-rain-water/
 *
 * Approach: Two pointers tracking max height from left (leftMax) and right (rightMax).
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

public class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;

        int left = 0, right = height.length - 1;
        int leftMax = height[left], rightMax = height[right];
        int water = 0;

        while (left < right) {
            if (leftMax < rightMax) {
                left++;
                leftMax = Math.max(leftMax, height[left]);
                water += leftMax - height[left];
            } else {
                right--;
                rightMax = Math.max(rightMax, height[right]);
                water += rightMax - height[right];
            }
        }

        return water;
    }

    // --- Test ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1})); // 6
    }
}
