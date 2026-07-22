"""
Problem: Group Anagrams
LeetCode #: 49
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

Approach: Use a hash map where key is character frequency tuple of 26 letters and value is list of anagram strings.
Time Complexity: O(N * K) where N is the number of strings and K is maximum length of a string.
Space Complexity: O(N * K) to store string groups in hash map.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
