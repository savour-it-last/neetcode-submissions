class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        # We recursively call till empty
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            # So we insert value in all possible locations
            for i in range(len(p)+1):
                p_copy  = p.copy()
                # We are recursing by skipping left value
                # so when we backtrack we gotta insert that excluded
                # value in all locations
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
