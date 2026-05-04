class Solution:
    def findMin(self, nums: List[int]) -> int:
        return Bin(nums,len(nums)-1,0)




def Bin(nums,high,low):
    while high>low:
        mid=(high+low)//2
        if high==low+1:
            return min(nums[high],nums[low])
        if nums[mid]<nums[(mid-1+len(nums))%len(nums)] and nums[mid]<nums[(mid+1+len(nums))%len(nums)]:
            return nums[mid]
        if nums[mid]>nums[low] and nums[mid]<nums[high]:
            return Bin(nums,mid-1,low)
        if nums[mid]>nums[low] and nums[mid]>nums[high]:
            return Bin(nums,high,mid+1)
        if nums[mid]<nums[low] and nums[mid]<nums[high]:
            return Bin(nums,mid-1,low)
    return nums[high]