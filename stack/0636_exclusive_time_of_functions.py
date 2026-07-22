"""
Problem: Exclusive Time of Functions
LeetCode #: 636
Difficulty: Medium
Link: https://leetcode.com/problems/exclusive-time-of-functions/

Approach:
Use a stack to keep track of active function calls.
Parse each log into `(fn_id, status, timestamp)`.
Maintain `prev_time` representing start of current execution interval.
- When a function starts:
  - If a function is currently executing on top of stack, add `timestamp - prev_time` to its exclusive time.
  - Push current `fn_id` onto stack and update `prev_time = timestamp`.
- When a function ends:
  - Pop `fn_id` from stack, add `timestamp - prev_time + 1` to its exclusive time.
  - Update `prev_time = timestamp + 1`.

Time Complexity: O(L) where L is the number of logs.
Space Complexity: O(N) stack size for active function calls.
"""

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []  # stores fn_id
        prev_time = 0

        for log in logs:
            parts = log.split(":")
            fn_id = int(parts[0])
            status = parts[1]
            timestamp = int(parts[2])

            if status == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:  # "end"
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return res
