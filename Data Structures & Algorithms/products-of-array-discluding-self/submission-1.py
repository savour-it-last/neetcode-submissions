class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        product = 1
        zero_count = 0
        zero_index = None
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
            else:
                zero_index = i
                zero_count += 1
                if zero_count >1:
                    return output
            
        if zero_count == 1 and zero_index is not None:
            output[zero_index] = product
            return output

        for i in range(len(nums)):
            output[i] = int(product/nums[i])
        
        return output



        