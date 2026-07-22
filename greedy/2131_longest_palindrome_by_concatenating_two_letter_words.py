"""
Problem: Longest Palindrome by Concatenating Two Letter Words
LeetCode #: 2131
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

Approach: Count word frequencies. Pair reversed asymmetric 2-letter words. Pair symmetric 2-letter words, reserving at most one odd symmetric word for the exact center.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        has_central = False
        
        for word, cnt in count.items():
            if word[0] == word[1]:
                length += (cnt // 2) * 4
                if cnt % 2 == 1:
                    has_central = True
            elif word[0] < word[1]:
                rev = word[1] + word[0]
                if rev in count:
                    length += min(cnt, count[rev]) * 4
                    
        if has_central:
            length += 2
            
        return length
