class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        stack.append(0)
        temp_ind = 1
        while temp_ind < len(temperatures):
            if stack and temperatures[stack[-1]] < temperatures[temp_ind]:
                res[stack[-1]] = temp_ind - stack[-1]
                stack.pop()
            else:
                stack.append(temp_ind)
                temp_ind+=1
        
        return res
            

            