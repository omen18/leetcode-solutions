"""
Problem: Maximize the Confusion of an Exam
LeetCode #: 2024
Difficulty: Medium
Link: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

Approach: Sliding window helper function finding max consecutive characters ('T' or 'F') achievable with at most `k` flips. Return max of both.
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_for_char(target_char: str) -> int:
            left = 0
            flips = 0
            max_len = 0
            for right in range(len(answerKey)):
                if answerKey[right] != target_char:
                    flips += 1
                while flips > k:
                    if answerKey[left] != target_char:
                        flips -= 1
                    left += 1
                max_len = max(max_len, right - left + 1)
            return max_len

        return max(max_for_char('T'), max_for_char('F'))
