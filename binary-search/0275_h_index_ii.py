"""
Problem: H-Index II
LeetCode #: 275
Difficulty: Medium
Link: https://leetcode.com/problems/h-index-ii/

Approach: Binary search on sorted citations finding boundary where citations[mid] >= n - mid.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if citations[mid] >= n - mid:
                high = mid - 1
            else:
                low = mid + 1
        return n - low


if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([0, 1, 3, 5, 6]))  # 3
