"""
Problem: Sqrt(x)
LeetCode #: 69
Difficulty: Easy
Link: https://leetcode.com/problems/sqrtx/

Approach: Binary search between 0 and x to find greatest integer whose square <= x.
Time Complexity: O(log x)
Space Complexity: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low, high = 1, x // 2
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))  # 2
    print(sol.mySqrt(8))  # 2
