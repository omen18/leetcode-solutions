"""
Problem: Convert Sorted Array to Binary Search Tree
LeetCode #: 108
Difficulty: Easy
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Approach: Recursive binary partition selecting mid element as subtree root.
Time Complexity: O(n)
Space Complexity: O(log n)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    root = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(root.val)  # 0
