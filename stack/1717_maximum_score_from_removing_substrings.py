"""
Problem: Maximum Score From Removing Substrings
LeetCode #: 1717
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-score-from-removing-substrings/

Approach:
Greedy approach: remove the substring with the higher points first to maximize total score,
then remove the other substring from remaining characters.
Use a helper function with a stack to perform pair removals:
- If `x >= y`, remove all "ab" patterns first (gain x), then remove "ba" patterns from remaining (gain y).
- If `y > x`, remove all "ba" patterns first (gain y), then remove "ab" patterns from remaining (gain x).

Time Complexity: O(N) two linear passes over string s.
Space Complexity: O(N) for stack.
"""

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(text: str, first: str, second: str, points: int):
            stack = []
            score = 0
            for char in text:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return "".join(stack), score

        total_score = 0
        if x >= y:
            s, score1 = remove_pair(s, 'a', 'b', x)
            _, score2 = remove_pair(s, 'b', 'a', y)
            total_score = score1 + score2
        else:
            s, score1 = remove_pair(s, 'b', 'a', y)
            _, score2 = remove_pair(s, 'a', 'b', x)
            total_score = score1 + score2

        return total_score
