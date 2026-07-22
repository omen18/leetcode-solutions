"""
Problem: Binary Tree Cameras
LeetCode #: 0968
Difficulty: Hard
Link: https://leetcode.com/problems/binary-tree-cameras/

Approach: Bottom-up greedy DFS with 3 node states:
0: Uncovered (needs camera)
1: Has camera
2: Covered (no camera here, but monitored)
If any child is uncovered (0), parent must have camera.
If any child has camera (1), parent is covered (2).
Otherwise, parent is uncovered (0).
If root ends up uncovered, place a camera at root.
Time Complexity: O(N)
Space Complexity: O(H)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cameras = 0

        # Returns state: 0=uncovered, 1=has_camera, 2=covered
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal cameras
            if not node:
                return 2

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                cameras += 1
                return 1

            if left == 1 or right == 1:
                return 2

            return 0

        if dfs(root) == 0:
            cameras += 1

        return cameras
