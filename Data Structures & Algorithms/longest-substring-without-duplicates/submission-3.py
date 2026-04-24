class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest_seq = 1
        left = 0
        right = 1
        substring = ""
        while right < len(s):
            substring = s[left]
            while right<len(s) and s[right] not in substring:
                substring += s[right]
                right+=1
            substring_length = len(substring)
            if longest_seq < substring_length:
                longest_seq = substring_length
            left = left + 1
            right = left + 1
        if len(substring) > longest_seq:
            longest_seq = len(substring)
        return longest_seq
