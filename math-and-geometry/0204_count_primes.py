"""
Problem: Count Primes
LeetCode #: 204
Difficulty: Medium
Link: https://leetcode.com/problems/count-primes/

Approach: Sieve of Eratosthenes algorithm. Mark multiples of each prime starting from i*i up to n as composite.
Time Complexity: O(n * log(log n))
Space Complexity: O(n)
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                is_prime[i * i : n : i] = [False] * len(range(i * i, n, i))

        return sum(is_prime)
