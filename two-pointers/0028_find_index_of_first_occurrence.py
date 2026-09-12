"""
Problem: Find the Index of the First Occurrence in a String
LeetCode #: 28
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Approach: Sliding window check of substring needle against haystack slices.
Time Complexity: O(n * m)
Space Complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))  # 0
    print(sol.strStr("leetcode", "leeto"))  # -1
