"""
Problem: Recover a Tree From Preorder Traversal
LeetCode #: 1028
Difficulty: Hard
Link: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

Approach: Stack-based iterative parser.
Count dashes to determine current node depth D.
Pop stack until len(stack) == D. Attach new node to stack[-1]'s left (if empty) or right.
Push new node to stack.
Time Complexity: O(N)
Space Complexity: O(H)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack: List[TreeNode] = []
        i = 0
        n = len(traversal)

        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1

            node = TreeNode(val)

            while len(stack) > depth:
                stack.pop()

            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

        return stack[0] if stack else None
