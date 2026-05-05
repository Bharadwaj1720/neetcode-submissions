class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        goal=n-1
        i=0
        count=0
        while i !=goal:
            if nums[i]+i>=goal:
                goal=i
                i=-1
                count+=1
            i+=1
        return count


        