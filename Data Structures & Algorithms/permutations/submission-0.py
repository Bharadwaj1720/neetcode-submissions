class Solution:
    def __init__(self):
        self.ans=[]
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.test([],nums)
        return self.ans
    def test(self,array,nums):
        n=len(nums)
        if n==0:
            self.ans.append(array)
            return
        for i in range(n):
            self.test(array+[nums[i]],nums[:i]+nums[i+1:])

        
        