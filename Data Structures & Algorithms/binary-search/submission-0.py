class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                res = middle
                break
            elif nums[middle]<target:
                left = middle+1
            else:
                right = middle - 1
        return res
        