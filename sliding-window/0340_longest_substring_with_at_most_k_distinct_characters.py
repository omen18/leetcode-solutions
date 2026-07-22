"""
Problem: Longest Substring with At Most K Distinct Characters
LeetCode #: 340
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Approach: Sliding Window + Hash Map. Maintain character frequency in a hash map. Expand right pointer; whenever distinct character count exceeds k, shrink left pointer until distinct count <= k.
Time Complexity: O(N)
Space Complexity: O(K)
"""

from typing import List
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0

        counts = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
