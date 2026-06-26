class Solution:
    def _spiral_layer(
        self, matrix: list[list[int]], layer: int, row_limiter: int, col_limiter: int
    ) -> list[int]:
        """
        Gets a single spirals values in order.
        If matrix is n*n, it will have n-1 layers from observation.
        """
        # Its always gonna start from 0,0 or 1,1.
        curr_row, curr_col = layer, layer

        layer_spiral_vals = []
        row_range = row_limiter - (2*layer)
        col_range = col_limiter - (2*layer)
        # Edge case handling ifs. NOTE: The end val is included cause it adds only 1 list into it.
        # If row range is 1, it means its only till the right end of layer
        # If only 1 value exists the below two conditions are valid so will insert single value in list.
        if row_range == 1:
            for _ in range((col_limiter - (2 * layer))):
                layer_spiral_vals.append(matrix[curr_row][curr_col])
                curr_col += 1
            return layer_spiral_vals
        # if col range is 1, it means its only till bottom end of layer
        if col_range == 1:
            for _ in range((row_limiter - (2 * layer))):
                layer_spiral_vals.append(matrix[curr_row][curr_col])
                curr_row += 1
            return layer_spiral_vals
        # traverse to the right starting from current except last value.
        # last value added at the start of next loop
        for _ in range((col_limiter - (2 * layer) - 1)):
            layer_spiral_vals.append(matrix[curr_row][curr_col])
            curr_col += 1

        for _ in range((row_limiter - (2 * layer) - 1)):
            layer_spiral_vals.append(matrix[curr_row][curr_col])
            curr_row += 1

        for _ in range((col_limiter - (2 * layer) - 1)):
            layer_spiral_vals.append(matrix[curr_row][curr_col])
            curr_col -= 1

        for _ in range((row_limiter - (2 * layer) - 1)):
            layer_spiral_vals.append(matrix[curr_row][curr_col])
            curr_row -= 1

        return layer_spiral_vals

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col_n = len(matrix[0])
        row_n = len(matrix)
        res = []
        # when I checked, it seems smallest val is what determines
        # number of layers
        layer_val = min(col_n, row_n)
        if layer_val % 2 == 0:
            layers = layer_val // 2
        else:
            layers = layer_val // 2 + 1

        for layer in range(layers):
            res.extend(
                self._spiral_layer(matrix=matrix, layer=layer, row_limiter=row_n, col_limiter=col_n)
            )

        return res
