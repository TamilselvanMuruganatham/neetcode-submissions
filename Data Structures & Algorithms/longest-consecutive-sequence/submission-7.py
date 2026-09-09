class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lookup_hash=set(nums)
        longest=0
        
        for num in nums:
            if num-1 in lookup_hash:
                continue
            length=0
            while num+length in lookup_hash:
                length+=1
            longest=max(longest,length) 
        
        return longest
