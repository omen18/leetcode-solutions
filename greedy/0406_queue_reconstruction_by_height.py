"""
Problem: Queue Reconstruction by Height
LeetCode #: 406
Difficulty: Medium
Link: https://leetcode.com/problems/queue-reconstruction-by-height/

Approach: Sort people by height in descending order, then by count k in ascending order. Insert each person into output list at index k.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
