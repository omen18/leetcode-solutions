"""
Problem: Clone Graph
LeetCode #: 133
Difficulty: Medium
Link: https://leetcode.com/problems/clone-graph/

Approach: Use Depth-First Search (DFS) with a hash map to maintain a mapping from original nodes to their cloned counterparts. Recursively clone unvisited nodes and populate neighbors.
Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
Space Complexity: O(V) for the hash map and recursion stack.
"""

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {}

        def dfs(curr: 'Node') -> 'Node':
            if curr in cloned:
                return cloned[curr]
            
            copy = Node(curr.val)
            cloned[curr] = copy
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
