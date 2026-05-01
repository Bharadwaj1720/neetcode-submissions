class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [-1]*128
        maxi=0
        temp=0
        start=0
        for i in range(len(s)):
            k=arr[ord(s[i])]
            if k>=start:
                if temp>maxi:
                    maxi=temp
                start=k+1
                temp=i-start+1
            else:
                temp+=1
            arr[ord(s[i])]=i
        if temp>maxi:
            maxi=temp
            
        return maxi

        