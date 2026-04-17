class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left <= right:
            if s[left].isalnum() is False:
                left+=1
                # We dont compare these
                continue

            if s[right].isalnum() is False:
                right-=1
                # we dont compare these
                continue

            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        
        return True

            
        