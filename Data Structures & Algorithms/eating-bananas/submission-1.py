class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        low=1
        old=(low+high)//2
        while low<=high:
            k=(low+high)//2
            print(k)
            flag=self.check(piles,h,k)
            if flag:
                high=k-1
                old=k
            else:
                low=k+1
            
        return old



    def check(self,piles,h,k):
        temp=0
        for i in piles:
            temp+=math.ceil(i/k)
        if temp<=h:
            return True
        else:
            return False
        