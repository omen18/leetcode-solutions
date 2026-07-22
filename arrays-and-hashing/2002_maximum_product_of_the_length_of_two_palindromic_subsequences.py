"""
Problem: Maximum Product of the Length of Two Palindromic Subsequences
LeetCode #: 2002
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

Approach: Bitmask enumeration for string length N <= 12. Precompute palindromic subsequence lengths and find max product of disjoint mask pairs.
Time Complexity: O(2^N * N + 2^(2N)) which is very fast for N <= 12.
Space Complexity: O(2^N) for palindrome map.
"""


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palindromes = {}

        for mask in range(1, 1 << n):
            subseq = [s[i] for i in range(n) if (mask & (1 << i))]
            if subseq == subseq[::-1]:
                palindromes[mask] = len(subseq)

        max_prod = 0
        items = list(palindromes.items())

        for i in range(len(items)):
            mask1, len1 = items[i]
            for j in range(i + 1, len(items)):
                mask2, len2 = items[j]
                if (mask1 & mask2) == 0:
                    max_prod = max(max_prod, len1 * len2)

        return max_prod
