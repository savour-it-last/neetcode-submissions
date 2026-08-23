
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # string s we assign map to each letter
        # then for the second string 
        s_map = {}
        t_map = {}

        if len(s) != len(t):
            return False

        for c1,c2 in zip(s,t):
            if c1 not in s_map:
                s_map[c1] = 0
            if c2 not in t_map:
                t_map[c2] = 0
            s_map[c1]+=1
            t_map[c2]+=1
        
        return t_map == s_map



