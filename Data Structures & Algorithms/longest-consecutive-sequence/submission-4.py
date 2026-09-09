class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lookup_hash=set(nums)
        nums=sorted(lookup_hash)
        max_consecutive=0
        count=1
        for num in nums:
            if num+1 in lookup_hash:
                count += 1
            else:
                max_consecutive=max(max_consecutive,count)
                count=1
            
        max_consecutive=max(max_consecutive,count)
        
        return max_consecutive
