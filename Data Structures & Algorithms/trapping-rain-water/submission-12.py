class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l,r, res = 0, len(height)-1, 0
        maxL, maxR = height[l], height[r]
        while l<r:
            if maxL<maxR:
                l+=1
                maxL = max(maxL, height[l])
                # if maxL is smaller below will be zero thas all.
                # same for right
                res+= maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        
        return res


        
            
            
            
            