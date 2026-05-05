class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        self.dp=['?']*(n+1)
        self.dp[0]=0
        self.dp[1]=0
        self.temp(len(cost),cost)
        return self.dp[n]
    def temp(self,n,cost):
        if n<=1:
            return self.dp[n]
        if self.dp[n]=='?':
            k=min(self.temp(n-1,cost)+cost[n-1],self.temp(n-2,cost)+cost[n-2])
            self.dp[n]=k
        return self.dp[n]