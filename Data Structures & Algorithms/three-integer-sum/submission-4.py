class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        target=0
        k=set()
        
        for i in range(len(nums)):
            k=self.twoPointer(nums[i+1:],nums[i],k)
        for j in k:
            ans.append([j[0],j[1],j[2]])
        return ans



    def twoPointer(self,nums,target,ans):
        n=len(nums)
        p=0
        q=n-1
        while p<q:
            k=nums[p]+nums[q]
            if k==-target:
                ans.add((nums[p],nums[q],target))
                p+=1
                q-=1
                continue
            if k<-target:
                p+=1
            else:
                q-=1
        return ans
        