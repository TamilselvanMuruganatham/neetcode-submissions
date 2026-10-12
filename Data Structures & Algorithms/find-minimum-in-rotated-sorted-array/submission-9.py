class Solution:
    def findMin(self, nums: List[int]) -> int:
        minValue=float('inf')
        left=0
        right=len(nums)-1
        if right == 0 : 
            return nums[right]
        while left<right:
            
            mid=(left+right)//2
            leftValue, rightValue=nums[left],nums[right]
            midValue=nums[mid]
            if midValue>rightValue:
                minValue=min(rightValue,minValue)
                left=mid+1
            else:
                minValue=min(leftValue,minValue)
                right=mid
        return minValue

