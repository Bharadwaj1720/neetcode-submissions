class Solution:
    def __init__(self):
        self.ans=[]
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.test([],nums,0,target)
        unique_data = [list(x) for x in set(tuple(x) for x in self.ans)]
        return unique_data

    def test(self,array,nums,i,target):
        n=len(nums)
        if i>=n:
            return
        if target==0:
            self.ans.append(array)
            return
        if target>=nums[i]:
            self.test(array+[nums[i]],nums,i+1,target-nums[i])
            self.test(array+[nums[i]],nums,i,target-nums[i])
        self.test(array,nums,i+1,target)
        