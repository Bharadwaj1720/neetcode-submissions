class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operands=['+','-','*','/']
        for i in tokens:
            if i not in operands:
                stack.append(i)
            else:
                if i=='+':
                    temp=int(stack[-2])+int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(temp))
                if i=='-':
                    temp=int(stack[-2])-int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(temp))
                if i=='*':
                    temp=int(stack[-2])*int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(temp))
                if i=='/':
                    temp=int(int(stack[-2])/int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(str(temp))
            print(stack)
        return int(stack[-1])



        