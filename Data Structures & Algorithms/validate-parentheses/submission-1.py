class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            
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
        
        if len(stk)!=0:
            return False
        return True    
            
        