"""
Problem: Word Search
LeetCode #: 79
Difficulty: Medium
Link: https://leetcode.com/problems/word-search/

Approach: Backtracking / 2D DFS. Start depth-first search from every grid cell matching word[0]. Temporarily mark visited cells in-place with '#' to avoid revisit, then backtrack (restore cell) when returning.
Time Complexity: O(M * N * 3^L) where M, N are grid dimensions and L is word length.
Space Complexity: O(L) for recursion stack.
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (dfs(r + 1, c, idx + 1) or
                     dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or
                     dfs(r, c - 1, idx + 1))
            
            board[r][c] = temp
            return found
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
