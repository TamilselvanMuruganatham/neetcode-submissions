class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        if nums[start]==target:
            return start
        if nums[end]==target:return end

        while start<end:
            mid_index=start+(end-start)//2
            mid_number=nums[mid_index]
            if mid_number == target:
                return mid_index
            if nums[start]<target<mid_number:
                end-=1
            else:
                start+=1
            
        return -1

