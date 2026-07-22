"""
Problem: Task Scheduler
LeetCode #: 621
Difficulty: Medium
Link: https://leetcode.com/problems/task-scheduler/

Approach: Use a Max-Heap to always execute the task with the highest remaining frequency,
and a Queue to store cooling down tasks along with the time when they become available again.
At each time unit, check if a task in the queue is ready to re-enter the max-heap.
If max-heap has available tasks, pop the highest frequency task, decrement frequency, and if > 0 enqueue with (freq, time + n).

Time Complexity: O(N) where N is total tasks
Space Complexity: O(1) since there are at most 26 unique tasks
"""

from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
