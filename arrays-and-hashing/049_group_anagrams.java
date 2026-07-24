/*
 * Problem: Group Anagrams
 * LeetCode #: 49
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/group-anagrams/
 *
 * Approach: Categorize strings by sorted character array as key in a HashMap.
 * Time Complexity: O(n * k log k) where n is number of strings and k is max length.
 * Space Complexity: O(n * k)
 */

import java.util.*;

public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = String.valueOf(ca);
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(s);
        }
        return new ArrayList<>(map.values());
    }

    // --- Test ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println(sol.groupAnagrams(strs));
    }
}
