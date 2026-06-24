class Solution:
    def _layer_rotation(self, matrix: list[list[int]], curr_row: int, matrix_len: int)->None:
        """
        For a given layer we do 4 way rotation for all values of 
        curr_row until n-1-offset column val is reached.
        Offset is basically just curr_row + 1 tbh so lets not 
        keep a separate variable
        """
        # starting position is always gonna be  equal nah
        curr_col = curr_row
        col = curr_col
        # Now for the layer we gotta do from curr_col upt matrix_len-1-(curr_row+1)
        # where curr_row + 1 is offset
        while curr_col <= (matrix_len - 1) - (curr_row+1):
            # recalibrate row to curr_row when u iterate col,
            # Thats why its inside the loop
            row = curr_row
            col = curr_col
            store_val = matrix[row][col]
            for _ in range(4):
                new_row = col
                new_col = matrix_len - 1 - row
                # Store store_val in new r and c, and store that value in store_val
                matrix[new_row][new_col], store_val = store_val, matrix[new_row][new_col]
                row = new_row
                col = new_col
            curr_col+=1
        return None

    def rotate(self, matrix: List[List[int]]) -> None:
        # (old_col, n-1-old_row)
        # swapping is tough for above
        # transpose + reverse is the way for easier code, below is intuitive solution
        row=0
        col=0
        top = [row,col]
        n = len(matrix[0])
        # n//2 cause we gotta do only for first half.
        # if even number lets say 4, we do 0, 1
        # for odd lets say 5, we do 0,1 and skip 2 which is fine since its center
        while row<(n//2):
            self._layer_rotation(matrix=matrix, curr_row=row, matrix_len=n)
            row+=1
        return None
            
            


            