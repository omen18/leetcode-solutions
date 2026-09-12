"""
Problem: Word Break II
LeetCode #: 140
Difficulty: Hard
Link: https://leetcode.com/problems/word-break-ii/

Approach: DFS with memoization to find all valid sentences segmented from dictionary.
Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def dfs(sub):
            if sub in memo:
                return memo[sub]
            if not sub:
                return [""]
            res = []
            for word in words:
                if sub.startswith(word):
                    suffix = sub[len(word):]
                    for rest in dfs(suffix):
                        res.append(f"{word}{' ' if rest else ''}{rest}")
            memo[sub] = res
            return res

        return dfs(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
