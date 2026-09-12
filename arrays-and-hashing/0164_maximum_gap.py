"""
Problem: Maximum Gap
LeetCode #: 164
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-gap/

Approach: Pigeonhole bucket sort in linear time and space.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        min_v, max_v, n = min(nums), max(nums), len(nums)
        if min_v == max_v:
            return 0
        b_size = max(1, (max_v - min_v) // (n - 1))
        b_count = (max_v - min_v) // b_size + 1
        buckets = [[float("inf"), float("-inf")] for _ in range(b_count)]
        for x in nums:
            idx = (x - min_v) // b_size
            buckets[idx][0] = min(buckets[idx][0], x)
            buckets[idx][1] = max(buckets[idx][1], x)
        max_gap = 0
        prev_max = min_v
        for b_min, b_max in buckets:
            if b_min == float("inf"):
                continue
            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max
        return max_gap


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumGap([3, 6, 9, 1]))  # 3
