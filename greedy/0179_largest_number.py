"""
Problem: Largest Number
LeetCode #: 179
Difficulty: Medium
Link: https://leetcode.com/problems/largest-number/

Approach: Custom comparator sorting pairs by comparing string concatenation order (x + y vs y + x).
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s_nums = list(map(str, nums))
        s_nums.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        res = "".join(s_nums)
        return "0" if res[0] == "0" else res


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber([10, 2]))  # "210"
