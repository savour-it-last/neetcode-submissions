class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_dict = {}
        for n in nums:
            if n not in n_dict:
                n_dict[n] = 1
                continue
            return True
        return False