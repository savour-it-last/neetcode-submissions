class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # First get all point with 0
        first_col_zeros = False
        first_row_zeroes = False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col == 0 and matrix[row][col] == 0:
                    first_col_zeros = True

                if row == 0 and matrix[row][col] == 0:
                    first_row_zeroes = True

                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # if the values are in the sets make em zero
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                # makes full row zero

                if matrix[row][0] == 0:
                    matrix[row][col] = 0
                    # break cause all cols of that row are made 0 anyway
                # we can only do for when that col is zero
                elif matrix[0][col] == 0: 
                    matrix[row][col] = 0
        if 0 == matrix[0][0] and first_row_zeroes:
            matrix[0] = [0]*len(matrix[0])
        
        if 0 == matrix[0][0] and first_col_zeros:
            for row in range(len(matrix)):
                matrix[row][0]=0



        
                
        
        