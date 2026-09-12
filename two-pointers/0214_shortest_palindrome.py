"""
Problem: Shortest Palindrome
LeetCode #: 214
Difficulty: Hard
Link: https://leetcode.com/problems/shortest-palindrome/

Approach: KMP prefix function on s + '#' + reversed(s) to find longest palindromic prefix.
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        combo = s + "#" + rev
        lps = [0] * len(combo)
        for i in range(1, len(combo)):
            j = lps[i - 1]
            while j > 0 and combo[i] != combo[j]:
                j = lps[j - 1]
            if combo[i] == combo[j]:
                j += 1
            lps[i] = j
        pal_len = lps[-1]
        return rev[:len(s) - pal_len] + s


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPalindrome("aacecaaa"))  # "aaacecaaa"
