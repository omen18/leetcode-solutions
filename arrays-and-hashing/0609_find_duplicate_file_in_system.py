"""
Problem: Find Duplicate File in System
LeetCode #: 609
Difficulty: Medium
Link: https://leetcode.com/problems/find-duplicate-file-in-system/

Approach: Parse paths into directory and file contents. Group full file paths by file content in hash map.
Time Complexity: O(N * L) where N is number of paths and L is average path string length.
Space Complexity: O(N * L) for storing paths in hash map.
"""

from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for path_str in paths:
            parts = path_str.split(" ")
            dir_path = parts[0]
            for file_info in parts[1:]:
                file_name, content = file_info.split("(")
                content = content[:-1]  # remove trailing ')'
                content_map[content].append(f"{dir_path}/{file_name}")

        return [files for files in content_map.values() if len(files) > 1]
