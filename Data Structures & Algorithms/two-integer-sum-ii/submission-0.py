class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p=0
        q=len(numbers)-1
        while p<q:
            k=numbers[p]+numbers[q]
            if k==target:
                return [p+1,q+1]
            if k<target:
                p+=1
            else:
                q-=1
        