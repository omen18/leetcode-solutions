"""
Problem: Ugly Number
LeetCode #: 263
Difficulty: Easy
Link: https://leetcode.com/problems/ugly-number/

Approach: Repeatedly divide positive integer by prime factors 2, 3, and 5.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.isUgly(6))   # True
    print(sol.isUgly(14))  # False
