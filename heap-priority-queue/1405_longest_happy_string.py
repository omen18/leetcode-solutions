"""
Problem: Longest Happy String
LeetCode #: 1405
Difficulty: Medium
Link: https://leetcode.com/problems/longest-happy-string/

Approach: Use a Max-Heap storing (-count, char) for available characters with count > 0.
In each iteration, pop the character with the highest remaining frequency.
If appending it to the result would create three identical consecutive characters, pop the second most frequent character instead.
Append the selected character to the result, decrement its count, and push it back into the heap if count > 0.
If the first character was temporarily skipped, push it back as well.

Time Complexity: O(a + b + c)
Space Complexity: O(1)
"""

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(max_heap, (-count, char))

        res = []

        while max_heap:
            cnt1, char1 = heapq.heappop(max_heap)

            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not max_heap:
                    break
                cnt2, char2 = heapq.heappop(max_heap)
                res.append(char2)
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(max_heap, (cnt2, char2))
                heapq.heappush(max_heap, (cnt1, char1))
            else:
                res.append(char1)
                cnt1 += 1
                if cnt1 < 0:
                    heapq.heappush(max_heap, (cnt1, char1))

        return "".join(res)
