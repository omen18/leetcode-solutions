/*
 * Problem: N-Queens II
 * LeetCode #: 52
 * Difficulty: Hard
 * Link: https://leetcode.com/problems/n-queens-ii/
 *
 * Approach: Backtracking to count valid queen placements using sets for column and diagonal attacks.
 * Time Complexity: O(N!)
 * Space Complexity: O(N)
 */

import java.util.HashSet;
import java.util.Set;

public class Solution {
    private int count = 0;

    public int totalNQueens(int n) {
        count = 0;
        Set<Integer> cols = new HashSet<>();
        Set<Integer> posDiag = new HashSet<>();
        Set<Integer> negDiag = new HashSet<>();

        backtrack(0, n, cols, posDiag, negDiag);
        return count;
    }

    private void backtrack(int r, int n, Set<Integer> cols, Set<Integer> posDiag, Set<Integer> negDiag) {
        if (r == n) {
            count++;
            return;
        }

        for (int c = 0; c < n; c++) {
            if (cols.contains(c) || posDiag.contains(r + c) || negDiag.contains(r - c)) {
                continue;
            }

            cols.add(c);
            posDiag.add(r + c);
            negDiag.add(r - c);

            backtrack(r + 1, n, cols, posDiag, negDiag);

            cols.remove(c);
            posDiag.remove(r + c);
            negDiag.remove(r - c);
        }
    }

    // --- Test ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println("N = 4 total solutions: " + sol.totalNQueens(4)); // 2
        System.out.println("N = 8 total solutions: " + sol.totalNQueens(8)); // 92
    }
}
