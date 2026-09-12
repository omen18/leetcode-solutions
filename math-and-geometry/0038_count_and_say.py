"""
Problem: Count and Say
LeetCode #: 38
Difficulty: Medium
Link: https://leetcode.com/problems/count-and-say/

Approach: Iterative run-length encoding generation of consecutive identical characters.
Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        seq = "1"
        for _ in range(n - 1):
            next_seq = []
            i = 0
            while i < len(seq):
                count = 1
                while i + 1 < len(seq) and seq[i] == seq[i + 1]:
                    i += 1
                    count += 1
                next_seq.append(f"{count}{seq[i]}")
                i += 1
            seq = "".join(next_seq)
        return seq


if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(4))  # "1211"
