"""
Problem: Merge Sorted Array
LeetCode #: 88
Difficulty: Easy
Link: https://leetcode.com/problems/merge-sorted-array/

Approach: Fill nums1 from the back using three pointers (p1 for nums1, p2 for nums2, p for target).
Time Complexity: O(m + n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


if __name__ == "__main__":
    sol = Solution()
    n1 = [1, 2, 3, 0, 0, 0]
    sol.merge(n1, 3, [2, 5, 6], 3)
    print(n1)  # [1, 2, 2, 3, 5, 6]
