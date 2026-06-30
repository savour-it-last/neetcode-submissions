class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        default_check_dict = {}
        true_dict = {}
        for c1 in s1:
            default_check_dict[c1] = 0
            true_dict[c1] = true_dict.get(c1, 0) + 1
        n2 = len(s2)
        n1 = len(s1)
        index = 0

        check_dict = default_check_dict.copy()
        while index<n2:
            if s2[index] in check_dict:  
                j = index
                while j< index + n1 and j < n2:
                    if s2[j] not in check_dict or check_dict[s2[j]] > true_dict[s2[j]]:
                        break
                    check_dict[s2[j]] += 1
                    j+=1

            if check_dict == true_dict:
                return True

            check_dict = default_check_dict.copy()
            index+=1
        return False

                