"""
Problem: Container With Most Water
LeetCode #: 11
Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/

Approach: Two pointers starting from ends. Move pointer pointing to shorter line inward.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


# --- Test ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
