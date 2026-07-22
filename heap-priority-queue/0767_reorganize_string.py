"""
Problem: Reorganize String
LeetCode #: 767
Difficulty: Medium
Link: https://leetcode.com/problems/reorganize-string/

Approach: Count character frequencies and use a Max-Heap storing (-count, char).
Pop the most frequent character, append it to the result, and hold it in a temporary variable (`prev`).
In the next step, push `prev` back into the max-heap if its count > 0, before picking the next character.
If at any point no character can be picked but `prev` is remaining, reorganization is impossible, return "".

Time Complexity: O(N log K) where K <= 26 is the number of distinct characters
Space Complexity: O(K)
"""

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = [(-cnt, char) for char, cnt in counts.items()]
        heapq.heapify(max_heap)

        prev_cnt, prev_char = 0, ""
        res = []

        while max_heap:
            cnt, char = heapq.heappop(max_heap)
            res.append(char)

            if prev_cnt < 0:
                heapq.heappush(max_heap, (prev_cnt, prev_char))

            prev_cnt, prev_char = cnt + 1, char

        result = "".join(res)
        return result if len(result) == len(s) else ""
