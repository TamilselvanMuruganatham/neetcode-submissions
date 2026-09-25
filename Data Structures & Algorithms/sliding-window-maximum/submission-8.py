from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        slide_window=deque()
        max_values=[]
        start=end=0
        while end<len(nums):
            num=nums[end]
            while slide_window and num>nums[slide_window[-1]]:
                
                slide_window.pop()
            slide_window.append(end)
            if (end-start)+1 == k:
                max_num=nums[slide_window[0]]
                max_values.append(max_num)
                
                if start ==slide_window[0]:
                    slide_window.popleft()
                start+=1
            end+=1
        return max_values

      
      
        
        

            
    



            


      