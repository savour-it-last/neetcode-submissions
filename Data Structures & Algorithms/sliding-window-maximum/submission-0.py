class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k
        res = []
        while right < len(nums)+1:
            res.append(max(nums[left:right]))
            left+=1
            right+=1
        
        return res
            