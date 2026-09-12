"""
Problem: Isomorphic Strings
LeetCode #: 205
Difficulty: Easy
Link: https://leetcode.com/problems/isomorphic-strings/

Approach: Ensure bidirectional bijection between characters of s and t.
Time Complexity: O(n)
Space Complexity: O(1) limited alphabet
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st, map_ts = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 in map_st and map_st[c1] != c2) or (c2 in map_ts and map_ts[c2] != c1):
                return False
            map_st[c1] = c2
            map_ts[c2] = c1
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))  # True
    print(sol.isIsomorphic("foo", "bar"))  # False
