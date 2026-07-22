"""
Problem: Fraction to Recurring Decimal
LeetCode #: 166
Difficulty: Medium
Link: https://leetcode.com/problems/fraction-to-recurring-decimal/

Approach: Long division with hash map to detect repeating remainder patterns.
Time Complexity: O(Denominator)
Space Complexity: O(Denominator)
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        # Sign handling
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        num = abs(numerator)
        den = abs(denominator)

        # Integer part
        res.append(str(num // den))
        rem = num % den

        if rem == 0:
            return "".join(res)

        res.append(".")
        seen = {}  # remainder -> index in res

        while rem != 0:
            if rem in seen:
                res.insert(seen[rem], "(")
                res.append(")")
                break

            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // den))
            rem %= den

        return "".join(res)
