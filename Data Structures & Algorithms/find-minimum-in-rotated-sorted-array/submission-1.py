class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums)-1
        left = 0
        middle = (left + right)//2
        while left<right:
            middle = (left + right)//2
            if nums[middle] >= nums[right]:
                left = middle + 1
            elif nums[middle] < nums[right]:
                right = middle
        return nums[left]
