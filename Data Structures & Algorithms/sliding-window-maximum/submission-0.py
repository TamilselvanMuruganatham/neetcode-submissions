class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start=0
        end=k
        max_values=[]
        while end<=len(nums):
            max_values.append (
                max(nums[start:end]))
            start+=1
            end+=1
        return max_values