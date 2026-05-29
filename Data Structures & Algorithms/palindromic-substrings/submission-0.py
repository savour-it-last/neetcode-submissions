class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_list = []
        for i in range(len(s)):
            left, right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome_list.append(s[left:right+1])
                left-=1
                right+=1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome_list.append(s[left:right+1])
                left-=1
                right+=1
        return len(palindrome_list)
        