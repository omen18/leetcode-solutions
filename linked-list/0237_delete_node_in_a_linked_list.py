"""
Problem: Delete Node in a Linked List
LeetCode #: 237
Difficulty: Medium
Link: https://leetcode.com/problems/delete-node-in-a-linked-list/

Approach: Copy value of next node into current node and skip the next node.
Time Complexity: O(1)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    sol = Solution()
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(1)
    n1.next = n2
    n2.next = n3
    sol.deleteNode(n2)
    print(n1.next.val)  # 1
