class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        start=0
        index=k+start
        iter_index=start
        max_value=nums[iter_index]
        max_opts=[]
        while iter_index<len(nums):
            max_value=max(max_value,nums[iter_index])
            iter_index+=1
            if iter_index==index:
                max_opts.append(max_value)
                max_value=nums[iter_index] if iter_index<len(nums) else nums[-1]
                start+=1
                index+=1
                iter_index=start
        return max_opts
        
        
        