class Solution:
    def consumed_in_time(self, piles: list[int], h: int, rate: int)->bool:
        count = 0
        for pile in piles:
            remainder = pile % rate
            if remainder:
                count+= (pile + (rate - remainder))//rate
            else:
                count += pile //rate
        if count>h:
            return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        min_rate = 1
        res = float("+infinity")
        while min_rate<=max_rate:
            curr_rate = (max_rate+min_rate)//2
            if self.consumed_in_time(piles=piles, h=h, rate=curr_rate):
                res = min(res, curr_rate)
                max_rate = curr_rate - 1
            else:
                min_rate = curr_rate+1
        return res


            

        