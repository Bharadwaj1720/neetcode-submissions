class Solution:
    def __init__(self):
        self.ans=[]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.test([],nums,0)
        return self.ans

    def test(self,array,nums,i):
        n=len(nums)
        if i>=n:
            self.ans.append(array)
            return
        self.test(array+[nums[i]],nums,i+1)
        self.test(array,nums,i+1)

        