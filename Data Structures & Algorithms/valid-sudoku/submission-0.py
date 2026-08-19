class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        box = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num == ".":
                    continue
                
                box_index = (i // 3) * 3 + j // 3
                
                if (num in row[i] or
                    num in column[j] or
                    num in box[box_index]):
                    return False
                
                row[i].add(num)
                column[j].add(num)
                box[box_index].add(num)
        return True
        