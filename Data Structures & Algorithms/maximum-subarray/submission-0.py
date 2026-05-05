class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=-10000
        n=len(nums)
        curr=0
        for i in range(n):
            curr+=nums[i]
            ans=max(ans,curr)
            if curr<0:
                curr=0
        return ans


        