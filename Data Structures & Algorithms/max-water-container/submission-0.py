class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        start,end=0,len(heights)-1
        while start<end:
            distance = end-start
            water= min(heights[start],heights[end])*distance

            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1

            max_water=max(max_water,water)
        return max_water
        
