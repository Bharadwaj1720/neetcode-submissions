class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hashmap=[0]*10
            for j in range(9):
                if board[i][j]!='.':  
                    if hashmap[int(board[i][j])]==1:
                        return False
                    hashmap[int(board[i][j])]+=1
            hashmap=[0]*10
            for j in range(9):
                if  board[j][i]!='.': 
                    if hashmap[int(board[j][i])]==1:
                        return False
                    hashmap[int(board[j][i])]+=1
        hashmap1=[0]*10
        hashmap2=[0]*10
        hashmap3=[0]*10
        for i in range(0,3):
            for j in range(0,3):
                if  board[i][j]!='.': 
                    if hashmap1[int(board[i][j])]==1:
                        return False
                    hashmap1[int(board[i][j])]+=1
            for j in range(3,6):
                if  board[i][j]!='.': 
                    if hashmap2[int(board[i][j])]==1:
                        return False
                    hashmap2[int(board[i][j])]+=1
            for j in range(6,9):
                if  board[i][j]!='.': 
                    if hashmap3[int(board[i][j])]==1:
                        return False
                    hashmap3[int(board[i][j])]+=1

        hashmap1=[0]*10
        hashmap2=[0]*10
        hashmap3=[0]*10
        for i in range(3,6):
            for j in range(0,3):
                if  board[i][j]!='.':
                    if hashmap1[int(board[i][j])]==1:
                        return False
                    hashmap1[int(board[i][j])]+=1
            for j in range(3,6):
                if  board[i][j]!='.': 
                    if hashmap2[int(board[i][j])]==1:
                        return False
                    hashmap2[int(board[i][j])]+=1
            for j in range(6,9):
                if  board[i][j]!='.': 
                    if hashmap3[int(board[i][j])]==1:
                        return False
                    hashmap3[int(board[i][j])]+=1

        hashmap1=[0]*10
        hashmap2=[0]*10
        hashmap3=[0]*10
        for i in range(6,9):
            for j in range(0,3):
                if board[i][j]!='.': 
                    if hashmap1[int(board[i][j])]==1:
                        return False
                    hashmap1[int(board[i][j])]+=1
            for j in range(3,6):
                if board[i][j]!='.': 
                    if hashmap2[int(board[i][j])]==1:
                        return False
                    hashmap2[int(board[i][j])]+=1
            for j in range(6,9):
                if board[i][j]!='.': 
                    if hashmap3[int(board[i][j])]==1:
                        return False
                    hashmap3[int(board[i][j])]+=1
        return True


            

        


        