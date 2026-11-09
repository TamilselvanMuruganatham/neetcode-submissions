class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result=len(nums)
        i=0
        for num in nums:
            result ^= i^num
            i += 1
        return result