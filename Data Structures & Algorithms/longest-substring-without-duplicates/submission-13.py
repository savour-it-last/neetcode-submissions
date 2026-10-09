class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        counter = {}
        duplicates = 0
        maxlen = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right],0) + 1
            if counter[s[right]] == 2:
                duplicates+=1
            while duplicates:
                counter[s[left]]-=1
                if counter[s[left]] == 1:
                    duplicates-=1
                left+=1
            maxlen = max(maxlen, right-left+1)
        return maxlen

                
            
            
