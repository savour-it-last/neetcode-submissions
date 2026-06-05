class Solution:
    def _solve_for_subseq(self, curr_ind: int, prev_ind: int, nums: List[int]) -> int:
        """
        Starting from every nums we gotta check
        """
        if curr_ind >= len(nums):
            return 0

        if (curr_ind, prev_ind) in self.memory:
            return self.memory[(curr_ind, prev_ind)]

        # keep prev same and curr skips one val
        exclusive = self._solve_for_subseq(curr_ind=curr_ind + 1, prev_ind=prev_ind, nums=nums)
        inclusive = 0
        if prev_ind == -1 or nums[curr_ind] > nums[prev_ind]:
            inclusive += 1 + self._solve_for_subseq(
                curr_ind=curr_ind + 1, prev_ind=curr_ind, nums=nums
            )
        res = max(inclusive, exclusive)
        self.memory[(curr_ind, prev_ind)] = res
        return res

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.memory = {}
        return self._solve_for_subseq(curr_ind=0, prev_ind=-1, nums=nums)
