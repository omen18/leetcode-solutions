"""
Problem: Sort Items by Groups Respecting Dependencies
LeetCode #: 1203
Difficulty: Hard
Link: https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

Approach: Hierarchical (Two-Level) Topological Sorting.
1. Assign standalone group IDs (from m onwards) to items with `group[i] == -1`.
2. Construct both an item-level dependency graph and a group-level dependency graph.
3. Run Topological Sort independently on items and groups using Kahn's algorithm.
4. If cycle exists in either level, return `[]`.
5. Group sorted items by group ID and combine according to group order.

Time Complexity: O(V + E) where V = n + m and E is number of dependency entries in beforeItems.
Space Complexity: O(V + E) for graphs, in-degree arrays, and result buffers.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        num_groups = group_id

        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(list)
        group_indegree = [0] * num_groups

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        def topo_sort(
            nodes: List[int], graph: defaultdict, indegree: List[int]
        ) -> List[int]:
            queue = deque([node for node in nodes if indegree[node] == 0])
            res = []
            while queue:
                curr = queue.popleft()
                res.append(curr)
                for neighbor in graph[curr]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            return res if len(res) == len(nodes) else []

        item_order = topo_sort(list(range(n)), item_graph, item_indegree)
        group_order = topo_sort(list(range(num_groups)), group_graph, group_indegree)

        if not item_order or not group_order:
            return []

        grouped_items = defaultdict(list)
        for item in item_order:
            grouped_items[group[item]].append(item)

        res = []
        for g in group_order:
            res.extend(grouped_items[g])

        return res
