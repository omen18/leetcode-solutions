"""
Problem: Number of Distinct Substrings in a String
LeetCode #: 1698
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

Approach: Insert all suffixes of the string into a Trie. The number of created nodes (excluding root) equals the number of distinct substrings.
Time Complexity: O(N^2) where N is length of string s
Space Complexity: O(N^2) for Trie storage
"""


class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def countDistinct(self, s: str) -> int:
        root = TrieNode()
        count = 0

        for i in range(len(s)):
            node = root
            for j in range(i, len(s)):
                char = s[j]
                if char not in node.children:
                    node.children[char] = TrieNode()
                    count += 1
                node = node.children[char]

        return count
