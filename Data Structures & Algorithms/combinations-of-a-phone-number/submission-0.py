class Solution:
    def __init__(self):
        self.arr=[]
    def alpha(self,s):
        if s=='2':
            return ['a','b','c']
        if s=='3':
            
            return ['d','e','f']
        if s=='4':
            return ['g','h','i']
        if s=='5':
            return ['j','k','l']
        if s=='6':
            return ['m','n','o']
        if s=='7':
            return ['p','q','r','s']
        if s=='8':
            return ['t','u','v']
        if s=='9':
            return ['w','x','y','z']
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        self.temp(digits,'')
        return self.arr

    def temp(self,digits,s):
        if len(digits)==0:
            self.arr.append(s)
            return
        k=self.alpha(digits[0])
        
        for i in k:
            self.temp(digits[1:],s+i)
        

        