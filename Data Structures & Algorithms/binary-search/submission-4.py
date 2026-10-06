class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end=0,len(nums)-1
        
        while start<=end:
            mid_index=((end-start)//2)+start
            
            if nums[mid_index]==target:
                return mid_index
            elif nums[mid_index]>target:
                end-=1
            else :
                start+=1
        return -1