"""
Problem: Reverse String
LeetCode #: 344
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-string/

Approach: Two pointers swapping characters in-place from outer ends toward center.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    sol = Solution()
    ch = ["h", "e", "l", "l", "o"]
    sol.reverseString(ch)
    print(ch)  # ["o", "l", "l", "e", "h"]
