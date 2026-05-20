class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxar = 0
        i = 0
        j = len(heights) - 1
        
            
            
        while i < j:
            val = min(heights[i],heights[j]) * (j-i)
            if val > maxar: 
                    maxar = val       
            
            if heights[i] > heights[j]:
                    j-=1
            else:
                    i+=1
            
                
                        
        return maxar