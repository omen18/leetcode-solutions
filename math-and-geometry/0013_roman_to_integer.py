"""
Problem: Roman to Integer
LeetCode #: 13
Difficulty: Easy
Link: https://leetcode.com/problems/roman-to-integer/

Approach: Map symbols to values. If current symbol is smaller than next symbol, subtract; otherwise add.
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and val[s[i]] < val[s[i + 1]]:
                total -= val[s[i]]
            else:
                total += val[s[i]]
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))      # 3
    print(sol.romanToInt("LVIII"))    # 58
    print(sol.romanToInt("MCMXCIV"))  # 1994
