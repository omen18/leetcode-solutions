/*
 * Problem: Coin Change
 * LeetCode #: 322
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/coin-change/
 *
 * Approach: Bottom-up 1D Dynamic Programming table (dp[i] = min coins to make amount i).
 * Time Complexity: O(amount * len(coins))
 * Space Complexity: O(amount)
 */

import java.util.Arrays;

public class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
}
