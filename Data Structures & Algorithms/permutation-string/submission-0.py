class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l1=[0]*26
        l2=[0]*26
        n=len(s1)
        m=len(s2)
        for i in s1:
            l1[ord(i)-ord('a')]+=1
        for i in range(len(s1)):
            l2[ord(s2[i])-ord('a')]+=1
        if l1==l2:
            return True
       
        for i in range(n,m):
            l2[ord(s2[i])-ord('a')]+=1
            l2[ord(s2[i-n])-ord('a')]-=1
            if l1==l2:
                return True
        return False