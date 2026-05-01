class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        l=[]
        for i in range(n):
            l.append((position[i],speed[i]))
        l.sort()
        stk=[]
        for i in range(n):
            flag=True
            while flag:
               
                if len(stk)==0:
                    stk.append(l[i])
                    flag=False
                else:
                    k1=stk[-1]
                    k2=l[i]
                    dist=k2[0]-k1[0]
                    sp=k1[1]-k2[1]
                    if sp<=0:
                        stk.append(k2)
                        flag=False
                    else:
                        tc=dist/sp
                        tp=(target-k2[0])/k2[1]
                        
                        if tp>=tc:
                            stk.pop()
                        else:
                            stk.append(k2)
                            flag=False
        return len(stk)

