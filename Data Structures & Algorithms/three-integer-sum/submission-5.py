class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_triples = []
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while k > j:
                current_sum = nums[j] + nums[k] + nums[i]
                if current_sum == 0:
                    sum_zero_triplet = [nums[i], nums[j], nums[k]]
                    unique_triples.append(sum_zero_triplet)
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while k>j and nums[k] == nums[k+1]:
                        k -= 1
                    continue

                if current_sum < 0:
                    j += 1
                else:
                    k -= 1

        return unique_triples
