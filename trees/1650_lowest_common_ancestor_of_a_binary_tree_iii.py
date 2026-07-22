"""
Problem: Lowest Common Ancestor of a Binary Tree III
LeetCode #: 1650
Difficulty: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

Approach: Two-pointer technique analogous to finding the intersection of two linked lists.
Traverse up using parent pointers. When a pointer reaches None, redirect it to the start of the other node.
Time Complexity: O(H) where H is tree height.
Space Complexity: O(1)
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1
