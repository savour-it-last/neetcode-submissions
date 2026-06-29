class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_cols = set()
        # First get all point with 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
        
        # if the values are in the sets make em zero
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # makes full row zero
                if row in zero_rows:
                    matrix[row] = [0]*len(matrix[0])
                    # break cause all cols of that row are made 0 anyway
                    break
                # we can only do for when that col is zero
                elif col in zero_cols: 
                    matrix[row][col] = 0
        
        return None


        
                
        
        