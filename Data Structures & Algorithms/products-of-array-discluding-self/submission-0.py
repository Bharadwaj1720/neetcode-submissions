class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        n=len(nums)
        for i in range(1,n):
            prefix.append(prefix[-1]*nums[i-1])
        for i in range(n-2,-1,-1):
            suffix.append(suffix[-1]*nums[i+1])
        suffix.reverse()
        ans=[]
        for i in range(n):
            ans.append(prefix[i]*suffix[i])
        return ans


        