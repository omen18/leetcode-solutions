"""
Problem: Maximum Binary Tree
LeetCode #: 654
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-binary-tree/

Approach: Use a monotonic stack maintaining nodes in strictly decreasing value order. Iterate through elements:
- Pop elements smaller than current number; the last popped element becomes current node's left child.
- If stack is not empty, current node becomes the right child of stack's top node.
- Push current node to stack. Return stack[0] as root.
Time Complexity: O(N) where N is length of nums.
Space Complexity: O(N) for stack storage.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for num in nums:
            curr = TreeNode(num)
            while stack and stack[-1].val < num:
                curr.left = stack.pop()
            if stack:
                stack[-1].right = curr
            stack.append(curr)

        return stack[0] if stack else None
