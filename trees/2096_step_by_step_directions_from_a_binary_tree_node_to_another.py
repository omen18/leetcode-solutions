"""
Problem: Step-By-Step Directions From a Binary Tree Node to Another
LeetCode #: 2096
Difficulty: Medium
Link: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

Approach: Find root-to-node paths for startValue and destValue using DFS.
Find the longest common prefix of both paths (representing path to LCA).
Convert all remaining steps from start path to 'U' and append the remaining steps of dest path.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(curr: Optional[TreeNode], val: int, path: List[str]) -> bool:
            if not curr:
                return False
            if curr.val == val:
                return True

            path.append('L')
            if find_path(curr.left, val, path):
                return True
            path.pop()

            path.append('R')
            if find_path(curr.right, val, path):
                return True
            path.pop()

            return False

        start_path, dest_path = [], []
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)

        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        up_steps = 'U' * (len(start_path) - i)
        down_steps = ''.join(dest_path[i:])

        return up_steps + down_steps
