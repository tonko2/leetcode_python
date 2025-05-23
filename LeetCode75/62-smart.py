class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp, dpa = [1, 2] + [0] * n, [1] * n
        for i in range(2, n):
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dpa[i - 1]) % MOD
            dpa[i] = (dp[i - 2] + dpa[i - 1]) % MOD
        
        return dp[n - 1]