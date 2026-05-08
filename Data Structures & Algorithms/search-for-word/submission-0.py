class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.temp(board,word,[])

    def temp(self,board,word,array):
        if len(array)!=0:
            coord=array[-1]
        n=len(board)
        m=len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if len(array)==0:
                        if len(word)==1:
                            return True
                        else:
                            k=self.temp(board,word[1:],array+[(i,j)])
                            if k:
                                return k

                    elif ((i==coord[0]-1 and j==coord[1]) or (i==coord[0]+1 and j==coord[1]) or (i==coord[0] and j==coord[1]-1) or (i==coord[0] and j==coord[1]+1)) and (i,j) not in array:
                        if len(word)==1:
                            return True
                        else:
                            k=self.temp(board,word[1:],array+[(i,j)])
                            if k:
                                return k

        return False
        