"""
Problem: Factorial Trailing Zeroes
LeetCode #: 172
Difficulty: Medium
Link: https://leetcode.com/problems/factorial-trailing-zeroes/

Approach: Count total factors of 5 by repeated division by 5.
Time Complexity: O(log5 n)
Space Complexity: O(1)
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(5))   # 1
    print(sol.trailingZeroes(25))  # 6
