class Solution:
    def ways2solve(self, index: int, s: str) -> int:
        if index in self.dp:
            return self.dp[index]
        if s[index] == "0":
            return 0
        res = self.ways2solve(index=index+1, s=s)
        if (index+1 < len(s)) and (s[index] == "1" or (s[index] == "2" and s[index+1] in "0123456")):
            res += self.ways2solve(index=index+2, s=s)
        self.dp[index] = res
        return res

    def numDecodings(self, s: str) -> int:
        self.dp = {len(s): 1}
        self.valid_nums = [i for i in range(1, 27)]
        self.ways2solve(index=0, s=s)
        return self.ways2solve(index=0, s=s)

        

