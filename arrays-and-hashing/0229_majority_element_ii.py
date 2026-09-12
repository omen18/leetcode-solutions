"""
Problem: Majority Element II
LeetCode #: 229
Difficulty: Medium
Link: https://leetcode.com/problems/majority-element-ii/

Approach: Boyer-Moore Voting Algorithm with 2 candidates appearing more than n // 3 times.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2, count1, count2 = None, None, 0, 0
        for n in nums:
            if n == c1:
                count1 += 1
            elif n == c2:
                count2 += 1
            elif count1 == 0:
                c1, count1 = n, 1
            elif count2 == 0:
                c2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        return [c for c in (c1, c2) if c is not None and nums.count(c) > len(nums) // 3]


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))  # [3]
