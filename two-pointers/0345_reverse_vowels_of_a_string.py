"""
Problem: Reverse Vowels of a String
LeetCode #: 345
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-vowels-of-a-string/

Approach: Two pointers scanning from left and right swapping vowel occurrences.
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return "".join(chars)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseVowels("hello"))     # "holle"
    print(sol.reverseVowels("leetcode"))  # "leotcede"
