"""
Problem: Single-Threaded CPU
LeetCode #: 1834
Difficulty: Medium
Link: https://leetcode.com/problems/single-threaded-cpu/

Approach: Sort tasks with original index by enqueue time: (enqueueTime, processingTime, index).
Maintain current `time` and a Min-Heap storing (processingTime, index) for tasks available at `time`.
While tasks remain or min-heap is non-empty:
  1. If min-heap is empty and current task's enqueueTime > time, advance time to task's enqueueTime.
  2. Push all available tasks with enqueueTime <= time into min-heap.
  3. Pop task with shortest processingTime (and smallest index), add index to result, advance time.

Time Complexity: O(N log N)
Space Complexity: O(N)
"""

import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted([(enqueue, proc, i) for i, (enqueue, proc) in enumerate(tasks)])
        res = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or min_heap:
            if not min_heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]

            while i < n and sorted_tasks[i][0] <= time:
                heapq.heappush(min_heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
                i += 1

            proc_time, idx = heapq.heappop(min_heap)
            time += proc_time
            res.append(idx)

        return res
