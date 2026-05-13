class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.pacific=[]
        self.atlantic=[]
        self.visitedp=set()
        self.visiteda=set()
        self.heights=heights
        n=len(self.heights)
        m=len(self.heights[0])
        for i in range(len(self.heights)):
            for j in range(len(self.heights[0])):
                if i==0 or j==0:
                    self.pacific.append((i,j))
                    self.visitedp.add((i,j))
                if i==n-1 or j==m-1:
                    self.atlantic.append((i,j))
                    self.visiteda.add((i,j))
                
        self.bfs('p')
        self.bfs('a')
        tt= list(self.visitedp & self.visiteda)
        return [list(t) for t in tt]

    def bfs(self,ocean):
        n=len(self.heights)
        m=len(self.heights[0])
        if ocean=='p':
            while len(self.pacific)!=0:
                t=self.pacific.pop(0)
                if t[0]-1>=0 and (t[0]-1,t[1]) not in self.visitedp and self.heights[t[0]-1][t[1]]>=self.heights[t[0]][t[1]]:
                    self.visitedp.add((t[0]-1,t[1]))
                    self.pacific.append((t[0]-1,t[1]))

                if t[0]+1<n and (t[0]+1,t[1]) not in self.visitedp and self.heights[t[0]+1][t[1]]>=self.heights[t[0]][t[1]]:
                    self.visitedp.add((t[0]+1,t[1]))
                    self.pacific.append((t[0]+1,t[1]))

                if t[1]-1>=0 and (t[0],t[1]-1) not in self.visitedp and self.heights[t[0]][t[1]-1]>=self.heights[t[0]][t[1]]:
                    self.visitedp.add((t[0],t[1]-1))
                    self.pacific.append((t[0],t[1]-1))
                if t[1]+1<m and (t[0],t[1]+1) not in self.visitedp and self.heights[t[0]][t[1]+1]>=self.heights[t[0]][t[1]]:
                    self.visitedp.add((t[0],t[1]+1))
                    self.pacific.append((t[0],t[1]+1))
        else:
            while len(self.atlantic)!=0:
                t=self.atlantic.pop(0)
                if t[0]-1>=0 and (t[0]-1,t[1]) not in self.visiteda and self.heights[t[0]-1][t[1]]>=self.heights[t[0]][t[1]]:
                    self.visiteda.add((t[0]-1,t[1]))
                    self.atlantic.append((t[0]-1,t[1]))

                if t[0]+1<n and (t[0]+1,t[1]) not in self.visiteda and self.heights[t[0]+1][t[1]]>=self.heights[t[0]][t[1]]:
                    self.visiteda.add((t[0]+1,t[1]))
                    self.atlantic.append((t[0]+1,t[1]))

                if t[1]-1>=0 and (t[0],t[1]-1) not in self.visiteda and self.heights[t[0]][t[1]-1]>=self.heights[t[0]][t[1]]:
                    self.visiteda.add((t[0],t[1]-1))
                    self.atlantic.append((t[0],t[1]-1))
                if t[1]+1<m and (t[0],t[1]+1) not in self.visiteda and self.heights[t[0]][t[1]+1]>=self.heights[t[0]][t[1]]:
                    self.visiteda.add((t[0],t[1]+1))
                    self.atlantic.append((t[0],t[1]+1))
        

        