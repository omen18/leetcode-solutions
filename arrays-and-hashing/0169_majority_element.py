"""
Problem: Majority Element
LeetCode #: 169
Difficulty: Easy
Link: https://leetcode.com/problems/majority-element/

Approach: Boyer-Moore Voting Algorithm to find majority element in O(1) space.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))             # 3
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
