class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums=[]
        for i in matrix:
            nums+=i
        return BS(nums,len(nums)-1,0,target)
        

def BS(nums,high,low,target):
    if high<low:
        return False
    mid=(high+low)//2
    if nums[mid]==target:
        return True
    if nums[mid]>target:
        return BS(nums,mid-1,0,target)
    else:
        return BS(nums,high,mid+1,target)
