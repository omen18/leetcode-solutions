/*
 * Problem: Climbing Stairs
 * LeetCode #: 70
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/climbing-stairs/
 *
 * Approach: Dynamic programming / Fibonacci sequence (ways(n) = ways(n-1) + ways(n-2)).
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

public class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int first = 1, second = 2;
        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }

    // --- Test ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.climbStairs(3)); // 3
        System.out.println(sol.climbStairs(5)); // 8
    }
}
