"""
Problem: Maximum Frequency Stack
LeetCode #: 895
Difficulty: Hard
Link: https://leetcode.com/problems/freq-stack/

Approach:
Maintain:
1. `freq`: hash map tracking current frequency of each value.
2. `group`: hash map mapping frequency level `f` to a stack of values with frequency at least `f`.
3. `max_freq`: integer storing maximum frequency present in the stack.

Operations:
- `push(val)`: increment `freq[val]`, update `max_freq`, and push `val` onto `group[freq[val]]`.
- `pop()`: pop value from `group[max_freq]`, decrement `freq[val]`, and if `group[max_freq]` is empty, decrement `max_freq`.

Time Complexity: O(1) for both `push` and `pop` operations.
Space Complexity: O(N) where N is number of elements pushed into FreqStack.
"""

from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
