class Solution:
    def __init__(self):
        self.arr=[]
    def partition(self, s: str) -> List[List[str]]:
        self.test(s,[])
        return self.arr

    def test(self,s,array):
        n=len(s)
        if n==0:
            self.arr.append(array)
            return
        for i in range(1,n+1):
            if s[:i]==s[:i][::-1]:
                self.test(s[i:],array+[s[:i]])
        