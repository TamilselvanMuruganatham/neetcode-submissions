class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        slide_window=[]
        start=end=0
        max_values=[]
        while end<len(nums):
            num=nums[end]
            while slide_window:
                exst_index=slide_window[-1]
                if num>=nums[exst_index]:
                    slide_window.pop()
                else:
                    break
            slide_window.append(end)
            if (end-start)+1 == k:
                max_num=nums[slide_window[0]]
                max_values.append(max_num)
                
                if start in slide_window:
                    slide_window.remove(start)
                start+=1
            end+=1
        return max_values

      
      
        
        

            
    



            


      