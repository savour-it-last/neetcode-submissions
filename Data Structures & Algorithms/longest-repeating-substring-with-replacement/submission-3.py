class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # To get max occuring char
        mp = {}
        max_freq = 0
        left = 0
        res = 0
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = 1
            else:
                mp[s[i]] += 1
            max_freq = max(max_freq, mp[s[i]])
            replacements = i-left+1-max_freq
            while replacements > k:
                mp[s[left]]-=1
                left += 1
                replacements = i-left+1-max_freq
            res = max(res, i - left + 1)
        return res
                

        
            
            
                
            


        
        