class Solution:
    def _alphaNum(self, char):
            return(
                ord('A')<=ord(char)<=ord('Z') or
                ord('a')<=ord(char)<=ord('z') or
                ord('0')<=ord(char)<=ord('9')
            )

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left <= right:
            if self._alphaNum(s[left]) is False:
                left+=1
                # We dont compare these
                continue

            if self._alphaNum(s[right]) is False:
                right-=1
                # we dont compare these
                continue

            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        
        return True

            
        