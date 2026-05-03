class Solution:
    def isHappy(self, n: int) -> bool:
        k=set()
        while n not in k and n!=1:
            m=0
            k.add(n)
            while n !=0:
                r=n%10
                n=n//10
                m+=r*r
            n=m
            
         
        if n==1:
            return True
        return False