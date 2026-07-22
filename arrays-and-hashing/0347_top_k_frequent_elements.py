"""
Problem: Top K Frequent Elements
LeetCode #: 347
Difficulty: Medium
Link: https://leetcode.com/problems/top-k-frequent-elements/

Approach: Count frequency using hash map and place elements into bucket array indexed by frequency (bucket sort).
Time Complexity: O(N) where N is length of nums.
Space Complexity: O(N) for hash map and buckets.
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
