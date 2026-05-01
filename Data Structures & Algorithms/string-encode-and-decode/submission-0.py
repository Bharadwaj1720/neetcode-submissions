class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '€'
        ans=''
        for i in strs:
            ans+=delimiter+i+delimiter
        return ans

    def decode(self, s: str) -> List[str]:
        n=len(s)
        i=0
        delimiter='€'
        ans=[]
        print(s)
        while i<n:
            if s[i]==delimiter:
                j=i+1
                temp=''
                while s[j]!=delimiter:
                    
                    temp+=s[j]
                    j+=1
                ans.append(temp)
            i=j+1
        return ans

