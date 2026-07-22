"""
Problem: Accounts Merge
LeetCode #: 721
Difficulty: Medium
Link: https://leetcode.com/problems/accounts-merge/

Approach: Union-Find (Disjoint Set Union). Map each email to its root representative.
For each account, union the first email with all subsequent emails in that account.
Group emails by root parent, sort each group, and prepend the user's name.

Time Complexity: O(N * K * log(N * K)) where N is accounts count and K is max emails per account.
Space Complexity: O(N * K) for Union-Find mapping and grouped email storage.
"""

from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, i: str) -> str:
        if i not in self.parent:
            self.parent[i] = i
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: str, j: str) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        groups = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            groups[root].append(email)

        res = []
        for root, emails in groups.items():
            res.append([email_to_name[root]] + sorted(emails))

        return res
