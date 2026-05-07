class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxi=''
        for i in range(0,n):
            temp=s[i]
            p=i-1
            q=i+1
            while p>=0 and q<n and s[p]==s[q]:
                temp=s[p]+temp+s[q]
                p-=1
                q+=1
            if len(temp)>len(maxi):
                maxi=temp
        for i in range(0,n-1):
            if s[i]==s[i+1]:
                temp=s[i]+s[i]
                p=i-1
                q=i+2
                while p>=0 and q<n and s[p]==s[q]:
                    temp=s[p]+temp+s[q]
                    p-=1
                    q+=1
                if len(temp)>len(maxi):
                    maxi=temp
        return maxi

        