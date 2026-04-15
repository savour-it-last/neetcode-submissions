class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i,n in enumerate(nums):
            diff = target -  n
            if diff in diff_dict:
                return sorted([i, diff_dict[diff]])
            # store index as value
            diff_dict[n] = i
    
        