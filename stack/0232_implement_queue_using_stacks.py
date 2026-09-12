"""
Problem: Implement Queue using Stacks
LeetCode #: 232
Difficulty: Easy
Link: https://leetcode.com/problems/implement-queue-using-stacks/

Approach: Two stacks: in_stack for push and out_stack for amortized O(1) pop/peek.
Time Complexity: Amortized O(1)
Space Complexity: O(n)
"""

class MyQueue:
    def __init__(self):
        self.in_st = []
        self.out_st = []

    def push(self, x: int) -> None:
        self.in_st.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_st.pop()

    def peek(self) -> int:
        if not self.out_st:
            while self.in_st:
                self.out_st.append(self.in_st.pop())
        return self.out_st[-1]

    def empty(self) -> bool:
        return not self.in_st and not self.out_st


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # 1
    print(q.pop())    # 1
    print(q.empty())  # False
