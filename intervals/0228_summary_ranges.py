"""
Problem: Summary Ranges
LeetCode #: 228
Difficulty: Easy
Link: https://leetcode.com/problems/summary-ranges/

Approach: Two pointers tracking start and end of continuous integer segments.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i]}")
            i += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0, 1, 2, 4, 5, 7]))  # ["0->2", "4->5", "7"]
