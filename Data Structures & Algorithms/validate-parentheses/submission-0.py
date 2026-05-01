class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            print(stk,i)
            if i=='(' or i=='{' or i=='[':
                stk.append(i)
            elif i==')' and len(stk)!=0 and stk[-1]=='(':
                stk.pop()
            elif i=='}' and len(stk)!=0 and stk[-1]=='{':
                stk.pop()
            elif i==']' and len(stk)!=0 and stk[-1]=='[':
                stk.pop()
            else:
                return False
        print(stk)
        if len(stk)!=0:
            return False
        return True    
            
        