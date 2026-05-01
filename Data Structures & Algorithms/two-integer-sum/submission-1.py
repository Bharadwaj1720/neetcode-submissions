class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            hashset=set(nums[:i]+nums[i+1:])
            if target-nums[i] in hashset:
                for j in range(len(nums)):
                    if i!=j and nums[i]+nums[j]==target:
                        return [i,j]

        