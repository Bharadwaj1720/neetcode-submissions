class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        result=[]
        n=len(temperatures)
        for i in range(n-1,-1,-1):
            k=temperatures[i]
            while len(stk)!=0 and temperatures[stk[-1]]<=k:
                stk.pop()
            if len(stk)==0:
                result.insert(0,0)
            else:
                result.insert(0,stk[-1]-i)
            stk.append(i)
            
        return result