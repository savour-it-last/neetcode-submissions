class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if target >= nums[left] and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[right] > nums[middle]:
                if target <= nums[right] and target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
              
        return -1
                

