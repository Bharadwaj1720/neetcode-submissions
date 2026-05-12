class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        self.grid=grid
        self.time=-1
        self.visited= [[0 for _ in range(m)] for _ in range(n)]
        queue=[]
        for i in range(n):
            for j in range(m):
                if self.grid[i][j]==2:
                    queue.append((i,j))
                    self.visited[i][j]=1

        Flag=False
        if len(queue)==0:
            Flag=True
        self.bfs(queue)
        for i in range(n):
            for j in range(m):
                if self.grid[i][j]==1:
                    return -1
        if Flag:
            return 0
        return self.time
    def bfs(self,queue):
        if len(queue)==0:
            return
        n=len(self.grid)
        m=len(self.grid[0])
        self.time+=1
        nqueue=[]
        while len(queue) != 0:
            k=queue.pop(0)
            if k[0]-1>=0 and self.visited[k[0]-1][k[1]]==0 and self.grid[k[0]-1][k[1]]==1:
                self.grid[k[0]-1][k[1]]=2
                self.visited[k[0]-1][k[1]]=1
                nqueue.append((k[0]-1,k[1]))

            if k[0]+1<n and self.visited[k[0]+1][k[1]]==0 and self.grid[k[0]+1][k[1]]==1:
                self.grid[k[0]+1][k[1]]=2
                self.visited[k[0]+1][k[1]]=1
                nqueue.append((k[0]+1,k[1]))

            if k[1]-1>=0 and self.visited[k[0]][k[1]-1]==0 and self.grid[k[0]][k[1]-1]==1:
                self.grid[k[0]][k[1]-1]=2
                self.visited[k[0]][k[1]-1]=1
                nqueue.append((k[0],k[1]-1))

            if k[1]+1<m and self.visited[k[0]][k[1]+1]==0 and self.grid[k[0]][k[1]+1]==1:
                self.grid[k[0]][k[1]+1]=2
                self.visited[k[0]][k[1]+1]=1
                nqueue.append((k[0],k[1]+1))
        self.bfs(nqueue)
            