class Solution:
    def _get_max_index(self, nums: list[int], start_index: int, end_index: int)->index:
        max_index = start_index
        for ind in range(start_index, end_index+1):
            if nums[max_index] < nums[ind]:
                max_index = ind
        return max_index

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k-1
        res = []
        max_index = self._get_max_index(nums=nums, start_index=left, end_index=right)
        while right < len(nums):
            if max_index < left:
                max_index = self._get_max_index(nums=nums, start_index=left, end_index=right)
            else:
                if nums[max_index] < nums[right]:
                    max_index = right
            res.append(nums[max_index])
            left+=1
            right+=1
        
        return res
            