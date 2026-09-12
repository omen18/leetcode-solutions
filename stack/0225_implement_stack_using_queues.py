"""
Problem: Implement Stack using Queues
LeetCode #: 225
Difficulty: Easy
Link: https://leetcode.com/problems/implement-stack-using-queues/

Approach: Single queue rotated on each push to maintain LIFO head ordering.
Time Complexity: Push O(n), Pop/Top O(1)
Space Complexity: O(n)
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


if __name__ == "__main__":
    st = MyStack()
    st.push(1)
    st.push(2)
    print(st.top())    # 2
    print(st.pop())    # 2
    print(st.empty())  # False
