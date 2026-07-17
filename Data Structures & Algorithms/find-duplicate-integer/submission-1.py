class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_hash = {}
        for num in nums:
            if num not in nums_hash:
                nums_hash[num] = 1
            else:
                return num
        
        