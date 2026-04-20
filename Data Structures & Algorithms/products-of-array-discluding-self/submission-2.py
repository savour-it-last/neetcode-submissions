class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0]*n
        pref_prods = [0]*n
        suffix_prods = [0]*n
        res = [0]*n

        # since no prefix and suffix exist in these locations.
        pref_prods[0]=1
        suffix_prods[n-1] = 1

        for i in range(1,n):
            pref_prods[i] = nums[i-1]*pref_prods[i-1]

        for i in range(n-2, -1, -1):
            suffix_prods[i] = nums[i+1]*suffix_prods[i+1]

        for i in range(n):
            res[i] = pref_prods[i]*suffix_prods[i]

        return res

        