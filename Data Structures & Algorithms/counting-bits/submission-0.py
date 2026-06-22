class Solution:
    def _count_1s(self, num: int)->int:
        count = 0
        while num:
            count+=1
            num&=(num-1)
        return count

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self._count_1s(num=i))
        return res

        