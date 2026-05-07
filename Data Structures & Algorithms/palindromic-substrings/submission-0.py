class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        for i in range(0,n):
            temp=s[i]
            count+=1
            p=i-1
            q=i+1
            while p>=0 and q<n and s[p]==s[q]:
                temp=s[p]+temp+s[q]
                count+=1
                p-=1
                q+=1
        for i in range(0,n-1):
            if s[i]==s[i+1]:
                count+=1
                temp=s[i]+s[i]
                p=i-1
                q=i+2
                while p>=0 and q<n and s[p]==s[q]:
                    count+=1
                    temp=s[p]+temp+s[q]
                    p-=1
                    q+=1
        return count
        