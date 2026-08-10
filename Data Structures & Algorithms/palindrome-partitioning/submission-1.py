class Solution:
    def check_palindrome(
        self,
        start_index: int,
        end_index: int,
        s: str,
    ) -> bool:
        """
        Returns whether s[start_index:end_index+1] is a palindrome.

        Uses memoization so that each substring is checked
        at most once.
        """

        # Already computed.
        if self.memory[start_index][end_index] != -1:
            return self.memory[start_index][end_index]

        left = start_index
        right = end_index

        while left < right:
            if s[left] != s[right]:
                self.memory[start_index][end_index] = False
                return False

            left += 1
            right -= 1

        self.memory[start_index][end_index] = True
        return True

    def get_valid_partitions(
        self,
        partition: list[str],
        s: str,
        start_index: int,
    ) -> None:
        """
        Generates every valid palindrome partition beginning
        at start_index.
        """

        # Entire string has been partitioned.
        if start_index == len(s):
            self.res.append(partition.copy())
            return

        # Try every possible ending index for the next partition.
        for end_index in range(start_index, len(s)):
            # Only recurse if the chosen substring is a palindrome.
            if self.check_palindrome(
                start_index=start_index,
                end_index=end_index,
                s=s,
            ):
                partition.append(s[start_index : end_index + 1])

                self.get_valid_partitions(
                    partition=partition,
                    s=s,
                    start_index=end_index + 1,
                )

                # Backtrack.
                partition.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.res: list[list[str]] = []

        # -1  -> not computed
        # True  -> palindrome
        # False -> not palindrome
        self.memory = [
            [-1 for _ in range(len(s))]
            for _ in range(len(s))
        ]

        self.get_valid_partitions(
            partition=[],
            s=s,
            start_index=0,
        )

        return self.res