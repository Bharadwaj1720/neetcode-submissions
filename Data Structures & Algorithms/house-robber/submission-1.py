class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        self.dp=['?']*(n)
        self.dp[0]=nums[0]
        if n>1:
            self.dp[1]=max(nums[0],nums[1])
        self.temp(nums,n-1)

        return self.dp[n-1]

    def temp(self,nums,n):
        if n<=1:
            return self.dp[n]
        if self.dp[n]=='?':
            k=max(self.temp(nums,n-2)+nums[n],self.temp(nums,n-1))
            self.dp[n]=k
        return self.dp[n]
        