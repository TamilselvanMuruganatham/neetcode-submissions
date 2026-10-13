class Solution:
    def findMin(self, nums: List[int]) -> int:
        minValue=float('inf')
        left=0
        right=len(nums)-1
        if right == 0 : 
            return nums[right]
        while left<right:
            mid=(left + right)//2
            
            if nums[mid]>nums[right]:
                left=mid+1
                minValue=min(minValue,nums[right])
            else:
                right=mid
                minValue=min(minValue,nums[left])


            
        return minValue
            

