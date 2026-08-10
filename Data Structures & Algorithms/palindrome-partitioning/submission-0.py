class Solution:
    def check_palindrome(self, start_index, end_index, s: str) -> bool:
        left = start_index
        right = end_index
        res = True
        while left < right:
            if s[left] != s[right]:
                res = False
                break
            left += 1
            right -= 1
        self.memory[start_index][end_index] = res
        return res

    def get_valid_partitions(
        self, partition: list[str], s: str, start_index: int
    ) -> None:
        if start_index == len(s):
            self.res.append(partition)
            return None

        for i in range(start_index, len(s)):
            if self.memory[start_index][i] != -1:
                if self.memory[start_index][i]:
                    self.get_valid_partitions(
                        partition=partition + [s[start_index : i + 1]],
                        s=s,
                        start_index=i + 1,
                    )
            else:
                if self.check_palindrome(start_index=start_index, end_index=i, s=s):
                    self.get_valid_partitions(
                        partition=partition + [s[start_index : i + 1]],
                        s=s,
                        start_index=i + 1,
                    )

    def partition(self, s: str) -> List[List[str]]:
        start_index = 0
        end_index = 0
        self.memory = [[-1 for i in range(len(s))] for j in range(len(s))]
        self.res = []
        self.get_valid_partitions(partition=[], s=s,start_index=0)
        return self.res
