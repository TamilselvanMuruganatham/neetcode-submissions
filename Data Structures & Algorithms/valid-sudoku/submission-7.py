from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict =defaultdict(set)
        col_dict = defaultdict(set)
        table_dict = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                value = board[row][col]  # Fixed: changed from board[row,col]
                
                if value == '.':
                    continue
                    
                if ( value in row_dict[row] or
                 value in col_dict[col] or 
                 value in table_dict[(row // 3, col // 3)]):
                    return False  # Immediately return False if any duplicate exists
                    
                row_dict[row].add(value)
                col_dict[col].add(value)
                table_dict[(row // 3, col // 3)].add(value)
                
        return True