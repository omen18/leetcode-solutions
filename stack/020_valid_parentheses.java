/*
 * Problem: Valid Parentheses
 * LeetCode #: 20
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/valid-parentheses/
 *
 * Approach: Stack matching closing brackets to opening brackets.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') stack.push(')');
            else if (c == '{') stack.push('}');
            else if (c == '[') stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c) return false;
        }
        return stack.isEmpty();
    }

    // --- Test ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isValid("()[]{}")); // true
        System.out.println(sol.isValid("(]"));     // false
    }
}
