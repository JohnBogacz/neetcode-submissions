class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        subs = defaultdict(set)

        # row
        for i in range(len(board)): # row
            for j in range(len(board)): # col

                val = board[i][j]

                if val == '.':
                    continue
                
                if val in rows[i]:
                    return False
                else:
                    rows[i].add(val)
                
                if val in cols[j]:
                    return False
                else:
                    cols[j].add(val)
                
                box = (
                    i//3,
                    j//3
                )

                if val in subs[box]:
                    return False
                else:
                    subs[box].add(val)
        
        return True

                

                
