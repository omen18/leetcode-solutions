"""
Problem: Reverse Bits
LeetCode #: 190
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-bits/

Approach: Shift result left and append lowest bit of n across 32 iterations.
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596))  # 964176192
