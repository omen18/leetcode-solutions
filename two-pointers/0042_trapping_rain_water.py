"""
Problem: Trapping Rain Water
LeetCode #: 42
Difficulty: Hard
Link: https://leetcode.com/problems/trapping-rain-water/

Approach: Two pointers tracking max height from left (left_max) and right (right_max).
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water


# --- Test ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
