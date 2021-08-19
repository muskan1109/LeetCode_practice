# problem #96

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1, 2]
        
        if n <= 2: return dp[n]
        
        for i in range(3, n + 1):
            dp.append(0)
            for root in range(1, i + 1):
                dp[i] += dp[root - 1] * dp[i - root]
                
        return dp[n]