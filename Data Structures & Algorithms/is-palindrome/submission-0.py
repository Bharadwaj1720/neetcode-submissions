import itertools
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        hashmap = set(
            itertools.chain(
                string.ascii_lowercase,
                string.ascii_uppercase,
                string.digits
            )
        )
        s=s.lower()
        n=len(s)
        p=0
        q=n-1
        while p<q:
            
            if s[p] not in hashmap:
                p+=1
                continue
            if s[q] not in hashmap:
                q-=1
                continue
            if s[p]!=s[q]:
                return False
            p+=1
            q-=1
        return True
