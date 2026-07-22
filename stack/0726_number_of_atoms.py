"""
Problem: Number of Atoms
LeetCode #: 726
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-atoms/

Approach:
Use a stack of hash maps to handle nested chemical formulas with parentheses.
- Push an initial hash map onto stack to store counts for outermost level.
- Parse string `formula` with index `i`:
  - If '(': push new empty hash map onto stack.
  - If ')': parse trailing multiplicity number `mult` (default 1). Pop top hash map from stack,
    multiply all element counts in popped map by `mult`, and merge into current stack top map.
  - If upper case letter: parse element name (uppercase + optional lowercase letters) and count `cnt` (default 1).
    Add `cnt` to element in current stack top map.
- Finally, sort all atomic symbols alphabetically and format result string.

Time Complexity: O(N log N) where N is length of formula string (due to sorting unique atoms).
Space Complexity: O(N) for stack and element maps.
"""

from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i, n = 0, len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i]) if start < i else 1

                top = stack.pop()
                for elem, cnt in top.items():
                    stack[-1][elem] += cnt * mult
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[start:i]

                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                cnt = int(formula[start:i]) if start < i else 1

                stack[-1][elem] += cnt

        final_counts = stack[0]
        res = []
        for elem in sorted(final_counts.keys()):
            res.append(elem)
            if final_counts[elem] > 1:
                res.append(str(final_counts[elem]))

        return "".join(res)
