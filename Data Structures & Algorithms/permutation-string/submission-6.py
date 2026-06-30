class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        default_check_dict = {}
        true_dict = {}
        for num in range(ord('a'), ord('z')+1):
            default_check_dict[chr(num)] = 0

        true_dict = default_check_dict.copy()
        for c1 in s1:
            true_dict[c1]+=1
            
        n2 = len(s2)
        n1 = len(s1)
        index = 0

        check_dict = default_check_dict.copy()
        left, right = 0,0
        while right<n2 and left<n2:            
            while right < left + n1 and right < n2:
                check_dict[s2[right]]+=1
                right+=1

            if check_dict == true_dict:
                return True
             
            check_dict[s2[left]]-=1
            left+=1
            
        return False

                