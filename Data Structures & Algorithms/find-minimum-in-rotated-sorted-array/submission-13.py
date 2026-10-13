class Solution:
    def findMin(self, nums: List[int]) -> int:
        minValue=float('inf')
        left=0
        right=len(nums)-1
        if right == 0 : 
            return nums[right]
        while left<right:
            mid=(left + right)//2
            midValue=nums[mid]
            leftValue=nums[left]
            rightValue=nums[right]

            if midValue>rightValue:
                left=mid+1
                minValue=min(minValue,rightValue)
            else:
                right=mid
                minValue=min(minValue,leftValue)


            
        return minValue
            

