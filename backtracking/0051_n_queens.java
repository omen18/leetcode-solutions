/*
 * Problem: N-Queens
 * LeetCode #: 51
 * Difficulty: Hard
 * Link: https://leetcode.com/problems/n-queens/
 *
 * Approach: Backtracking placing one queen per row while tracking attacked columns,
 *           positive diagonals (r + c), and negative diagonals (r - c).
 * Time Complexity: O(N!)
 * Space Complexity: O(N^2)
 */

import java.util.*;

public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(board[i], '.');
        }

        Set<Integer> cols = new HashSet<>();
        Set<Integer> posDiag = new HashSet<>();
        Set<Integer> negDiag = new HashSet<>();

        backtrack(0, n, board, res, cols, posDiag, negDiag);
        return res;
    }

    private void backtrack(int r, int n, char[][] board, List<List<String>> res,
                           Set<Integer> cols, Set<Integer> posDiag, Set<Integer> negDiag) {
        if (r == n) {
            List<String> copy = new ArrayList<>();
            for (char[] row : board) {
                copy.add(new String(row));
            }
            res.add(copy);
            return;
        }

        for (int c = 0; c < n; c++) {
            if (cols.contains(c) || posDiag.contains(r + c) || negDiag.contains(r - c)) {
                continue;
            }

            cols.add(c);
            posDiag.add(r + c);
            negDiag.add(r - c);
            board[r][c] = 'Q';

            backtrack(r + 1, n, board, res, cols, posDiag, negDiag);

            cols.remove(c);
            posDiag.remove(r + c);
            negDiag.remove(r - c);
            board[r][c] = '.';
        }
    }

    // --- Test ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        List<List<String>> result = sol.solveNQueens(4);
        System.out.println("N = 4 Solutions Count: " + result.size());
        for (List<String> board : result) {
            for (String row : board) {
                System.out.println(row);
            }
            System.out.println();
        }
    }
}
