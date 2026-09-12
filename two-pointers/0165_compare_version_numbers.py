"""
Problem: Compare Version Numbers
LeetCode #: 165
Difficulty: Medium
Link: https://leetcode.com/problems/compare-version-numbers/

Approach: Compare dot-separated revision integers sequentially with zero padding.
Time Complexity: O(max(n, m))
Space Complexity: O(n + m)
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        n1, n2 = len(v1), len(v2)
        for i in range(max(n1, n2)):
            rev1 = v1[i] if i < n1 else 0
            rev2 = v2[i] if i < n2 else 0
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion("1.2", "1.10"))  # -1
    print(sol.compareVersion("1.01", "1.001"))  # 0
