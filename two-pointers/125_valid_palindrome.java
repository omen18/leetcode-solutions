/*
 * Problem: Valid Palindrome
 * LeetCode #: 125
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/valid-palindrome/
 *
 * Approach: Two pointers starting from start and end, advancing while ignoring non-alphanumeric chars.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

public class Solution {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) left++;
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right--;
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    // --- Test ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isPalindrome("A man, a plan, a canal: Panama")); // true
        System.out.println(sol.isPalindrome("race a car")); // false
    }
}
