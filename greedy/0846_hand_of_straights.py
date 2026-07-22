"""
Problem: Hand of Straights
LeetCode #: 846
Difficulty: Medium
Link: https://leetcode.com/problems/hand-of-straights/

Approach: Count frequency of cards. Iterate through unique cards in sorted order, forming consecutive groups of size groupSize starting from the smallest available card.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        count = Counter(hand)
        sorted_keys = sorted(count.keys())
        
        for key in sorted_keys:
            if count[key] > 0:
                needed = count[key]
                for i in range(groupSize):
                    if count[key + i] < needed:
                        return False
                    count[key + i] -= needed
                    
        return True
