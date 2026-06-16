class Solution:
    def pathways(self, m: int, n: int, max_m: int, max_n: int) -> int:
        if (m, n) in self.visited:
            return self.visited[(m, n)]
        if m == max_m and n == max_n:
            return 1
        count = 0
        directions = [[0, 1], [1, 0]]
        for direction in directions:
            dm = m + direction[0]
            dn = n + direction[1]
            if 0 <= dm <= max_m and 0 <= dn <= max_n:
                count += self.pathways(m=dm, n=dn, max_m=max_m, max_n=max_n)
        self.visited[(m, n)] = count
        return count

    def uniquePaths(self, m: int, n: int) -> int:
        self.visited = {}
        return self.pathways(m=0, n=0, max_m=m-1, max_n=n-1)
