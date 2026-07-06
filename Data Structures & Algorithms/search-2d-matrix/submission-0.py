class Solution:
    def binary_search(self, arr: list[int], target: int)-> bool:
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
        res = False
        for row in matrix:
            if target >= row[0] and target <=row[-1]:
                res = self.binary_search(arr=row, target=target)
                break
        return res
