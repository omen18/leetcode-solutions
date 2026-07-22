"""
Problem: Linked List Random Node
LeetCode #: 382
Difficulty: Medium
Link: https://leetcode.com/problems/linked-list-random-node/

Approach: Use Reservoir Sampling to choose a node randomly with equal probability 1/N in a single pass without knowing the list size ahead of time or storing nodes in memory.
Time Complexity: O(N) per getRandom call where N is the number of nodes.
Space Complexity: O(1) extra space.
"""

import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        curr = self.head
        chosen_val = curr.val
        i = 1

        while curr:
            # Probability 1/i to replace chosen_val with current node's val
            if random.randint(1, i) == 1:
                chosen_val = curr.val
            curr = curr.next
            i += 1

        return chosen_val
