class Solution:
    def local_binary_search(self, arr: list[int], target: int)-> bool:
        left = 0
        right = len(arr) - 1
        res = False
        while left <= right:
            middle = (left+right)//2
            if arr[middle] == target:
                res = True
                break
            elif arr[middle]<target:
                left=middle+1
            else:
                right = middle-1
        return res

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1 
        res = False
        while left<=right:
            middle = (left+right)//2
            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                res = self.local_binary_search(arr=matrix[middle], target=target)
                break
            elif target < matrix[middle][0]:
                right = middle - 1
            else:
                left = middle + 1
        return res
