"""
Problem: Contains Duplicate III
LeetCode #: 220
Difficulty: Hard
Link: https://leetcode.com/problems/contains-duplicate-iii/

Approach: Bucket sort where each bucket has width valueDiff + 1 with sliding window indexDiff.
Time Complexity: O(n)
Space Complexity: O(min(n, k))
"""

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        w = valueDiff + 1
        buckets = {}
        for i, num in enumerate(nums):
            m = num // w
            if m in buckets:
                return True
            if m - 1 in buckets and abs(num - buckets[m - 1]) <= valueDiff:
                return True
            if m + 1 in buckets and abs(num - buckets[m + 1]) <= valueDiff:
                return True
            buckets[m] = num
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))  # True
