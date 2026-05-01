class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return BS(nums,len(nums)-1,0,target)


def BS(nums,high,low,target):
    if high<low:
        return -1
    mid=(high+low)//2
    if nums[mid]==target:
        return mid
    if nums[mid]>target:
        return BS(nums,mid-1,0,target)
    else:
        return BS(nums,high,mid+1,target)

        