"""
Problem: Palindrome Number
LeetCode #: 9
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-number/

Approach: Negative numbers and non-zero numbers ending with 0 cannot be palindromes. Reconstruct the second half.
Time Complexity: O(log10 n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))   # True
    print(sol.isPalindrome(-121))  # False
    print(sol.isPalindrome(10))    # False
