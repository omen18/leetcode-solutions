"""
Problem: Longest Common Prefix
LeetCode #: 14
Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix/

Approach: Compare characters column by column across all strings in the list.
Time Complexity: O(S) where S is the sum of characters
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # ""
