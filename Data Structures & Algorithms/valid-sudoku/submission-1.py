import  numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board=np.array(board)
        row_dict={ x:set() for x in range(9)  }
        col_dict={x:set() for x in range(9)}
        table_dict={ (x,y):set()  for x in range(3) for y in range(3)}
        for row in range(9):
            for col in range(9):
                value= board[row,col]
                if value == '.':
                    continue
                if value in row_dict[row]: 
                    return False
                if value in col_dict[col]:
                    return False
                key=(row//3,col//3)
                if value in table_dict[key]:
                    return False
                table_dict[key].add(value)
                row_dict[row].add(value)
                col_dict[col].add(value)
        return True
