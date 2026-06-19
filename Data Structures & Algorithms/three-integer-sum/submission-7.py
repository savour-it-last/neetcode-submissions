class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        visited = set()
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            target = -nums[i]
            while left<right:
                curr_sum = nums[left] + nums[right]
                if curr_sum > target:
                    right-=1
                elif curr_sum < target:
                    left+=1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    if triplet not in res:
                        res.append(triplet)
                    left+=1
                    right-=1
        return res


        