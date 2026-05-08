class Solution:
    def __init__(self):
        self.ans=[]
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.test([],nums,0,target)
        return self.ans
    def test(self,array,nums,i,target):
        n=len(nums)
        if target==0:
            self.ans.append(array)
            return
        if i>=n:
            return
        if target>=nums[i]:
            self.test(array+[nums[i]],nums,i+1,target-nums[i])
        j=i+1
        while j<n and nums[j]==nums[i]:
            j+=1
        self.test(array,nums,j,target)
        
        