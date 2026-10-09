class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        counter = {}
        duplicates = 0
        maxlen = 0
        while right<len(s) and left<=right:
            if duplicates == 0:
                counter[s[right]] = counter.get(s[right], 0) + 1
                if counter[s[right]]>1:
                    duplicates+=1
                right+=1
            else:
                counter[s[left]]-=1
                if counter[s[left]]==1:
                    duplicates-=1
                left+=1
            if duplicates == 0:
                    maxlen = max(maxlen, right - left)
                
                
        return maxlen
                
            
            
