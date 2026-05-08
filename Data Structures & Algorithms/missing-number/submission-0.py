class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        x=0
        y=nums[0]
        for i in range(n+1):
            x^=i
        for i in range(1,n):
            y^=nums[i]
        return x^y

        