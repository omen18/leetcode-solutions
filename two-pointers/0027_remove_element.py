"""
Problem: Remove Element
LeetCode #: 27
Difficulty: Easy
Link: https://leetcode.com/problems/remove-element/

Approach: Two pointers: overwrite elements not equal to val at index k.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 3]
    k = sol.removeElement(nums, 3)
    print(k, nums[:k])  # 2, [2, 2]
