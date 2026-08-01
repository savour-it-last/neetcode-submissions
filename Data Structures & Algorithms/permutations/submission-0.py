class Solution:
    def propogate(
        self, 
        unused_list: list[int], 
        used: list[int], 
        n: int, 
    ) -> None:
        if n == len(used):
            self.res.append(used.copy())
            return 
        
        for unused in unused_list.copy():
            used.append(unused)
            unused_list.remove(unused)
            self.propogate(unused_list=unused_list, used=used, n=n)
            unused_list.append(unused)
            used.remove(unused)      


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.propogate(unused_list= nums.copy(), used=[], n = len(nums))
        return self.res
