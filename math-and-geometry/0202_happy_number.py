"""
Problem: Happy Number
LeetCode #: 202
Difficulty: Easy
Link: https://leetcode.com/problems/happy-number/

Approach: Detect cycle in sum-of-squares sequence using a hash set.
Time Complexity: O(log n)
Space Complexity: O(log n)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num:
                total += (num % 10) ** 2
                num //= 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))  # True
    print(sol.isHappy(2))   # False
