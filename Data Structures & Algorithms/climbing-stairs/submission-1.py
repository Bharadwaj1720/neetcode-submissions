class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp=['?']*(n+1)
        self.dp[0]=1
        self.dp[1]=1
        self.temp(n)
        return self.dp[n]
    def temp(self,n):
        if n<=1:
            return self.dp[n]
        if n>1:
            if self.dp[n]=='?':
                k=self.temp(n-1)+self.temp(n-2)
                self.dp[n]=k
            return self.dp[n]
        