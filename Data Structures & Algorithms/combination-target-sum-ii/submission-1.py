from typing import List


class Solution:
    def build_combinations(
        self,
        candidates: List[int],
        target: int,
        start_index: int,
        current_sum: int,
        current_combination: List[int],
    ) -> None:
        """
        Recursively builds all unique combinations whose sum equals target.

        start_index:
            The first candidate that may be chosen in this call.
            Every recursive call only considers elements after this index,
            ensuring each candidate is used at most once.
        """

        if current_sum == target:
            self.result.append(current_combination.copy())
            return

        for candidate_index in range(start_index, len(candidates)):
            candidate_value = candidates[candidate_index]

            # Since the array is sorted, every value after this one
            # will also be too large.
            if current_sum + candidate_value > target:
                break

            # Skip duplicate values at the SAME recursion depth.
            #
            # Example:
            # [1, 1, 2]
            #
            # At the root, we only want to start one branch with '1'.
            # After choosing the first 1, deeper recursive calls are still
            # allowed to choose the second 1.
            # So we are in a recursion condition where we are not at the start index
            # and value is same as previous we have explored it already.
            # so at a different depth, if value is same as previous it means
            #its visited
            if (
                candidate_index > start_index
                and candidate_value == candidates[candidate_index - 1]
            ):
                continue
            

            current_combination.append(candidate_value)

            self.build_combinations(
                candidates=candidates,
                target=target,
                start_index=candidate_index + 1,
                current_sum=current_sum + candidate_value,
                current_combination=current_combination,
            )

            current_combination.pop()

    def combinationSum2(
        self,
        candidates: List[int],
        target: int,
    ) -> List[List[int]]:
        candidates.sort()

        self.result: List[List[int]] = []

        self.build_combinations(
            candidates=candidates,
            target=target,
            start_index=0,
            current_sum=0,
            current_combination=[],
        )

        return self.result