"""
Problem: Gas Station
LeetCode #: 134
Difficulty: Medium
Link: https://leetcode.com/problems/gas-station/

Approach: If total gas is less than total cost, completion is impossible. Otherwise, iterate through stations tracking tank balance. Reset start index whenever tank becomes negative.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            if total_tank < 0:
                start_index = i + 1
                total_tank = 0
                
        return start_index
