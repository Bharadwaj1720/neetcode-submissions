class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap=[0]*26
        for i in s:
            hashmap[ord(i)-ord('a')]+=1
        for i in t:
            hashmap[ord(i)-ord('a')]-=1
        for x in hashmap:
            if x!=0:
                return False
        return True