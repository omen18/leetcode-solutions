"""
Problem: Bag of Tokens
LeetCode #: 948
Difficulty: Medium
Link: https://leetcode.com/problems/bag-of-tokens/

Approach: Sort tokens. Use two pointers to play smallest token face-up to gain score when power permits, or largest token face-down to gain power when score >= 1.
Time Complexity: O(N log N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        score = 0
        max_score = 0
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0 and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
                
        return max_score
