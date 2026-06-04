class Solution:
    def travers_s_end(self, char_ind: int, wordDict: list[str], s: str) -> bool:
        if char_ind == len(s):
            return True
        if char_ind in self.memory:
            return self.memory[char_ind]

        for w in wordDict:
            if (char_ind + len(w)) <= len(s) and s[char_ind : char_ind + len(w)] == w:
                if self.travers_s_end(char_ind=char_ind + len(w), wordDict=wordDict, s=s):
                    self.memory[char_ind] = True
                    return True
        self.memory[char_ind] = False          
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memory = {}
        return self.travers_s_end(char_ind=0, wordDict=wordDict, s=s)
