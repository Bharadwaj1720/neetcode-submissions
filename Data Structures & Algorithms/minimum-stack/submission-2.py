class MinStack:

    def __init__(self):
        self.pmin=[]
        self.data=[]


    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.pmin)==0 or self.pmin[-1]>=val:
            self.pmin.append(val)
        return None
        

    def pop(self) -> None:
        if self.data[-1]==self.pmin[-1]:
            self.pmin.pop()
        self.data.pop()
        return None
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.pmin[-1]
        
