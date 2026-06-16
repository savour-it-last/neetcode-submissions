class Solution:
    def solution(self, ind1: int, ind2: int, text1: str, text2: str) -> int:
        if ind1 == len(text1) or ind2 == len(text2):
            return 0
        if self.visited[ind1][ind2] != -1:
            return self.visited[ind1][ind2]
        count = 0
        if text1[ind1] == text2[ind2]:
            count += 1 + self.solution(ind1=ind1 + 1, ind2=ind2 + 1, text1=text1, text2=text2)
        else:
            # increment text1, get res
            count1 = self.solution(ind1=ind1 + 1, ind2=ind2, text1=text1, text2=text2)
            # increment text2, get res
            count2 = self.solution(ind1=ind1, ind2=ind2 + 1, text1=text1, text2=text2)
            # count should store the max
            count = max(count1, count2)
        self.visited[ind1][ind2] = count
        return count

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.visited = [[-1] * len(text2) for _ in range(len(text1))]
        return self.solution(ind1=0, ind2=0, text1=text1, text2=text2)
