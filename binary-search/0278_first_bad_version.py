"""
Problem: First Bad Version
LeetCode #: 278
Difficulty: Easy
Link: https://leetcode.com/problems/first-bad-version/

Approach: Binary search to find first version where isBadVersion(v) returns True.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def isBadVersion(version: int) -> bool:
    return version >= 4


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstBadVersion(5))  # 4
