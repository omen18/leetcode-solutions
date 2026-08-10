"""
Problem: N-Queens II
LeetCode #: 52
Difficulty: Hard
Link: https://leetcode.com/problems/n-queens-ii/

Approach: Backtracking to count valid queen placements using sets for column and diagonal attacks.
Time Complexity: O(N!)
Space Complexity: O(N)
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        def backtrack(r) -> int:
            if r == n:
                return 1

            count = 0
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                count += backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

            return count

        return backtrack(0)


# --- Test ---
if __name__ == "__main__":
    sol = Solution()
    print("N = 4 total solutions:", sol.totalNQueens(4))  # 2
    print("N = 8 total solutions:", sol.totalNQueens(8))  # 92
