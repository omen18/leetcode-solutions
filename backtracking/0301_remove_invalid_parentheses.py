"""
Problem: Remove Invalid Parentheses
LeetCode #: 301
Difficulty: Hard
Link: https://leetcode.com/problems/remove-invalid-parentheses/

Approach: Backtracking. First calculate the exact count of misplaced '(' (rem_l) and ')' (rem_r). Then backtrack, pruning paths that remove more parentheses than needed or create invalid prefix states.
Time Complexity: O(2^N)
Space Complexity: O(N) for recursion stack and string builder.
"""

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        rem_l = rem_r = 0
        for char in s:
            if char == '(':
                rem_l += 1
            elif char == ')':
                if rem_l > 0:
                    rem_l -= 1
                else:
                    rem_r += 1
                    
        result = set()
        
        def backtrack(index: int, left_count: int, right_count: int, l_rem: int, r_rem: int, path: List[str]) -> None:
            if index == len(s):
                if l_rem == 0 and r_rem == 0 and left_count == right_count:
                    result.add("".join(path))
                return
            
            char = s[index]
            
            if char == '(' and l_rem > 0:
                backtrack(index + 1, left_count, right_count, l_rem - 1, r_rem, path)
            elif char == ')' and r_rem > 0:
                backtrack(index + 1, left_count, right_count, l_rem, r_rem - 1, path)
                
            path.append(char)
            if char != '(' and char != ')':
                backtrack(index + 1, left_count, right_count, l_rem, r_rem, path)
            elif char == '(':
                backtrack(index + 1, left_count + 1, right_count, l_rem, r_rem, path)
            elif char == ')' and left_count > right_count:
                backtrack(index + 1, left_count, right_count + 1, l_rem, r_rem, path)
            path.pop()
            
        backtrack(0, 0, 0, rem_l, rem_r, [])
        return list(result)
