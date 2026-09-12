"""
Problem: Zigzag Conversion
LeetCode #: 6
Difficulty: Medium
Link: https://leetcode.com/problems/zigzag-conversion/

Approach: Simulate row traversal using a direction flag that reverses at row 0 and row numRows - 1.
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        curr_row, step = 0, 1
        for char in s:
            rows[curr_row] += char
            if curr_row == 0:
                step = 1
            elif curr_row == numRows - 1:
                step = -1
            curr_row += step
        return "".join(rows)


if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))  # "PAHNAPLSIIGYIR"
