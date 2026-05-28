class Solution:
    def expand(self, s: str,  left: int, right: int) -> None:
        while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > self.longest_len:
                    self.longest_pal = s[left: right+1]
                    self.longest_len = right - left + 1
                left-=1
                right+=1

    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        
        self.longest_pal = ""
        self.longest_len = 0
        for i in range(len(s)):
            left, right = i, i
            self.expand(s=s, left=left, right=right)
            left, right = i, i+1
            self.expand(s=s, left=left, right=right)

        return self.longest_pal

