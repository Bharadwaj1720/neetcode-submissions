class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        self.visited = [[0 for _ in range(m)] for _ in range(n)]
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and self.visited[i][j]==0:
                    count+=1
                    self.DFS(grid,i,j)
        return count



    def DFS(self,grid,i,j):
        n=len(grid)
        m=len(grid[0])
        self.visited[i][j]=1
        if i-1>=0 and grid[i-1][j]=='1' and self.visited[i-1][j]==0:
            self.DFS(grid,i-1,j)
        if i+1<n and grid[i+1][j]=='1' and self.visited[i+1][j]==0:
            self.DFS(grid,i+1,j)
        if j-1>=0 and grid[i][j-1]=='1' and self.visited[i][j-1]==0:
            self.DFS(grid,i,j-1)
        if j+1<m and grid[i][j+1]=='1' and self.visited[i][j+1]==0:
            self.DFS(grid,i,j+1)

        