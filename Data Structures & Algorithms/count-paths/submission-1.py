class Solution:
    def pathways(self, m: int, n: int, max_m: int, max_n: int) -> int:
        if (m, n) in self.visited:
            return self.visited[(m, n)]
        if m == max_m and n == max_n:
            return 1
        if m>max_m or n>max_n:
            return 0

        count = 0
        count += self.pathways(m=m+1, n=n, max_m=max_m, max_n=max_n)
        count += self.pathways(m=m, n=n+1, max_m=max_m, max_n=max_n)
        self.visited[(m, n)] = count
        return count

    def uniquePaths(self, m: int, n: int) -> int:
        self.visited = {}
        return self.pathways(m=0, n=0, max_m=m-1, max_n=n-1)
