"""
Problem: Maximum Swap
LeetCode #: 670
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-swap/

Approach: Record last occurrence of each digit. From left to right, swap first digit with largest digit appearing later.
Time Complexity: O(N) where N is total number of digits.
Space Complexity: O(N) to store digits array.
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}

        for i, d in enumerate(digits):
            val = int(d)
            for target in range(9, val, -1):
                if last.get(target, -1) > i:
                    digits[i], digits[last[target]] = digits[last[target]], digits[i]
                    return int("".join(digits))

        return num
