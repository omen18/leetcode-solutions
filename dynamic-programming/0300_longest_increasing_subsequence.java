/*
 * Problem: Longest Increasing Subsequence
 * LeetCode #: 300
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/longest-increasing-subsequence/
 *
 * Approach: Patience sorting / Binary search (O(n log n)) or 1D DP (O(n^2)).
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 */

import java.util.Arrays;

public class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;

        for (int x : nums) {
            int i = 0, j = size;
            while (i != j) {
                int m = (i + j) / 2;
                if (tails[m] < x) i = m + 1;
                else j = m;
            }
            tails[i] = x;
            if (i == size) size++;
        }

        return size;
    }
}
