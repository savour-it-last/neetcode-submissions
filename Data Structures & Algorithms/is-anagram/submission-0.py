class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        x_dict = {}
        y_dict = {}
        for x in s:
            if x in x_dict:
                x_dict[x]+=1
                continue
            x_dict[x] = 1
        
        for y in t:
            if y in y_dict:
                y_dict[y] += 1
                continue
            y_dict[y] = 1

        return x_dict == y_dict 


        