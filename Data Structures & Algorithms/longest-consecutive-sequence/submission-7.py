class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        streak = 0
        res = 0
        i = 0
        curr = sorted_nums[0]
        while i < len(sorted_nums):
            if sorted_nums[i]!=curr:
                curr = sorted_nums[i]
                streak= 0
            while i<len(sorted_nums) and sorted_nums[i]==curr:
                i+=1
            streak +=1
            curr+=1
            res = max(res,streak)         
        return res