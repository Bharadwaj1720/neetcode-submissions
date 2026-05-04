class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        self.visited = [[0 for _ in range(m)] for _ in range(n)]
        max_area=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and self.visited[i][j]==0:
                    area = self.DFS(grid,i,j,0)
                    max_area=max(area,max_area)
        return max_area



    def DFS(self,grid,i,j,area):
        n=len(grid)
        m=len(grid[0])
        area+=1
        self.visited[i][j]=1
        if i-1>=0 and grid[i-1][j]==1 and self.visited[i-1][j]==0:
            area+=self.DFS(grid,i-1,j,0)
        if i+1<n and grid[i+1][j]==1 and self.visited[i+1][j]==0:
            area+=self.DFS(grid,i+1,j,0)
        if j-1>=0 and grid[i][j-1]==1 and self.visited[i][j-1]==0:
            area+=self.DFS(grid,i,j-1,0)
        if j+1<m and grid[i][j+1]==1 and self.visited[i][j+1]==0:
            area+=self.DFS(grid,i,j+1,0)
        return area
        