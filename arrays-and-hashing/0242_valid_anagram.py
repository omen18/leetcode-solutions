"""
Problem: Valid Anagram
LeetCode #: 242
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

Approach: Frequency counter hashmap comparing character counts.
Time Complexity: O(n)
Space Complexity: O(1) limited 26 characters
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
