class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        maxi=0
        for i in nums:
            if i-1 not in hashset:
                temp=0
                k=i
                while k in hashset:
                    temp+=1
                    k+=1
               
                if maxi<temp:
                    maxi=temp
        return maxi
        