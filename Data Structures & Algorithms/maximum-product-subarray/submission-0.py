class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = float("-infinity")
        
        i = 0
        curr_prod = 1
        max_prod = float("-infinity")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i==j:
                    curr_prod = nums[i]
                else:
                    curr_prod*=nums[j]
                max_prod = max(curr_prod, max_prod)
        return max_prod
                
            
            
