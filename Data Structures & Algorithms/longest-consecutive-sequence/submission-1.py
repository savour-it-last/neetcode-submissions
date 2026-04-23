class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums)))
        longest_sequence_count = 0
        left = 0
        right = 1
        counter = 1
        if not nums:
            return counter-1
            
        while right < len(sorted_nums):
            if (sorted_nums[left] == sorted_nums[right] - 1): 
                counter+=1
            else:
                if longest_sequence_count<counter:
                    longest_sequence_count = counter
                counter = 1
            left+=1
            right+=1
        if longest_sequence_count<counter:
                    longest_sequence_count = counter
        return longest_sequence_count
            


        