class Solution:
    def __init__(self):
        self.ans=[]
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.test([],nums,0)
        return self.ans
    def test(self,array,nums,i):
        n=len(nums)
        if i>=n:
            self.ans.append(array)
            return
        self.test(array+[nums[i]],nums,i+1)
        j=i+1
        while j<n and nums[j]==nums[i]:
            j+=1
        self.test(array,nums,j)
        