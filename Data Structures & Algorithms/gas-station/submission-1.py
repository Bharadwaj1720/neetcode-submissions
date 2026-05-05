class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        if sum(gas)<sum(cost):
            return -1
        result=[]
        for i in range(n):
            result.append(gas[i]-cost[i])
        temp=0
        i=0
        r=0
        print(result)
        while i <n:
            temp+=result[i]
            if temp<0:
                temp=0
                r=i+1
            i=i+1
        return r

                 

        