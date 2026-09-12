"""
Problem: Construct Binary Tree from Inorder and Postorder Traversal
LeetCode #: 106
Difficulty: Medium
Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Approach: Pop root from end of postorder and split inorder using hashmap index.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}

        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        return helper(0, len(inorder) - 1)


if __name__ == "__main__":
    sol = Solution()
    t = sol.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(t.val)  # 3
