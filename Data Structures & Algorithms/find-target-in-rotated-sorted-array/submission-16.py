class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        if nums[left]==target:
            return left
        if nums[right] ==target:
            return right
        
        while left<right:
            leftValue=nums[left]
            rightValue=nums[right]
            mid=(left+right)//2
            midValue=nums[mid]
            if target==leftValue:
                return left
            elif target==rightValue:
                return right
            elif target == midValue:
                return mid
            
            if leftValue<=midValue:
                if leftValue<=target<midValue:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if rightValue>=target>midValue:
                    left=mid+1
                else:
                    right=mid-1
                
        return -1
        
        