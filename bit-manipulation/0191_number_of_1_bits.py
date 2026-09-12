"""
Problem: Number of 1 Bits
LeetCode #: 191
Difficulty: Easy
Link: https://leetcode.com/problems/number-of-1-bits/

Approach: Brian Kernighan's bit-clearing algorithm: n &= n - 1 clears lowest set bit.
Time Complexity: O(k) where k is count of set bits
Space Complexity: O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(11))   # 3
    print(sol.hammingWeight(128))  # 1
