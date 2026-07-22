"""
Problem: Alien Dictionary
LeetCode #: 269
Difficulty: Hard
Link: https://leetcode.com/problems/alien-dictionary/

Approach: Topological Sort via Kahn's Algorithm (BFS).
1. Collect all unique characters and set up adjacency sets and in-degrees.
2. Compare consecutive word pairs to find the first differing character and establish directed edges.
3. Validate prefix conditions (e.g. "abc" before "ab" is invalid).
4. Run BFS with a queue of zero-indegree characters. Return ordering if all characters are processed.

Time Complexity: O(C) where C is total sum of word lengths.
Space Complexity: O(1) bounded by fixed alphabet size of 26.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        queue = deque([char for char in in_degree if in_degree[char] == 0])
        res = []

        while queue:
            char = queue.popleft()
            res.append(char)

            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) < len(in_degree):
            return ""

        return "".join(res)
