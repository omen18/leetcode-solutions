"""
Problem: Word Search II
LeetCode #: 212
Difficulty: Hard
Link: https://leetcode.com/problems/word-search-ii/

Approach: Build Trie from words list. Perform DFS from each cell on grid matching against Trie, pruning matched words.
Time Complexity: O(M * N * 3^L) where M x N is board dimension, L is max word length
Space Complexity: O(W * L) where W is number of words, L is max word length
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r: int, c: int, parent: TrieNode):
            char = board[r][c]
            curr_node = parent.children[char]

            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Avoid duplicates

            board[r][c] = '#'  # Mark visited

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            board[r][c] = char  # Restore cell

            # Prune leaf node from Trie to optimize subsequent searches
            if not curr_node.children:
                del parent.children[char]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result
