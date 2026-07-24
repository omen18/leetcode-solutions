/*
 * Problem: Longest Consecutive Sequence
 * LeetCode #: 128
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/longest-consecutive-sequence/
 *
 * Approach: Add all numbers to a HashSet. For each number, check if it's the start
 *           of a sequence (!set.contains(num - 1)). Count length of sequence.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

import java.util.*;

public class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int longestStreak = 0;
        for (int num : numSet) {
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;
                while (numSet.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }
                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }
        return longestStreak;
    }

    // --- Test ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2})); // 4
    }
}
