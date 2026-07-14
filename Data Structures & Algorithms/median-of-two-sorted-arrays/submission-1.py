class Solution:
    def find_index_binary_search(self, nums: list[int], threshold: int) ->int:
        """
        return insertion find index for insertion
        """
        left = 0
        right = len(nums) - 1
        while left<=right:
            middle =(left+right)//2
            if nums[middle] == threshold:
                return middle
            elif nums[middle]<threshold:
                left = middle + 1
            else:
                right = middle - 1
        return left


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left_bias = 0
        for num in nums1:
            target_index = self.find_index_binary_search(nums=nums2[left_bias:], threshold=num)
            target_index += left_bias 
            left_bias = target_index
            nums2.insert(target_index, num)
        
        l = len(nums2)
        if l%2 == 0:
            median = (nums2[(l//2)-1] + nums2[(l//2)])/2
        else:
            median =  nums2[(l//2)]
        return median

