class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_num=set()
        for num in nums:
            if num in seen_num:
                return num
            seen_num.add(num)
