"""
Problem: Ugly Number II
LeetCode #: 264
Difficulty: Medium
Link: https://leetcode.com/problems/ugly-number-ii/

Approach: Three-pointer DP generating multiples of 2, 3, and 5 in sorted order.
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2 = i3 = i5 = 0
        for i in range(1, n):
            next2, next3, next5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            nxt = min(next2, next3, next5)
            ugly[i] = nxt
            if nxt == next2:
                i2 += 1
            if nxt == next3:
                i3 += 1
            if nxt == next5:
                i5 += 1
        return ugly[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.nthUglyNumber(10))  # 12
