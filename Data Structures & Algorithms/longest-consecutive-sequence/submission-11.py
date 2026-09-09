class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for num in nums:
            
            if num-1 in nums: 
                continue
            
            length=0
            current_num=num
            while current_num in nums:
                length+=1
                current_num+=1
            longest=max(longest,length)


        return longest
