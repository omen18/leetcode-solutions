"""
Problem: Unique Binary Search Trees II
LeetCode #: 95
Difficulty: Medium
Link: https://leetcode.com/problems/unique-binary-search-trees-ii/

Approach: Recursive divide and conquer building all Cartesian combinations of left and right subtrees.
Time Complexity: O(4^n / n^(1/2))
Space Complexity: O(4^n / n^(1/2))
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = build(start, i - 1)
                right_trees = build(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i, l, r)
                        all_trees.append(root)
            return all_trees

        return build(1, n)


if __name__ == "__main__":
    sol = Solution()
    trees = sol.generateTrees(3)
    print(len(trees))  # 5
