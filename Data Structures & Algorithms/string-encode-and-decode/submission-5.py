class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for i,string in enumerate(strs):
            res += f"{len(string)}#{string}"
        return res


    def decode(self, s: str) -> List[str]:
        str_list = []
        i=0
        while i <len(s):
            j = i
            count_str = ""
            while s[j] != "#":
                count_str +=s[j]
                j+=1
            count = int(count_str)
            i = j + 1
            if count == 0:
                str_list.append("")
            else:
                str_list.append(s[i:i+count])
            i+=count
        
        return str_list
            

