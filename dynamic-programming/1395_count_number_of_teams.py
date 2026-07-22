"""
Problem: Count Number of Teams
LeetCode #: 1395
Difficulty: Medium
Link: https://leetcode.com/problems/count-number-of-teams/

Approach: Dynamic Programming / Combinatorics. For each index `j` treated as the middle soldier of the team:
Count how many elements to the left have smaller/larger ratings, and how many to the right have smaller/larger ratings.
The total number of teams with middle soldier `j` is `(left_less * right_greater) + (left_greater * right_less)`.
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total_teams = 0

        for j in range(1, n - 1):
            left_less = left_greater = 0
            right_less = right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                elif rating[k] > rating[j]:
                    right_greater += 1

            total_teams += (left_less * right_greater) + (left_greater * right_less)

        return total_teams
