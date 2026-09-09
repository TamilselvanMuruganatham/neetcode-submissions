class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if sum(nums)==target:
            return [0,1]
        lookup_dict={}
        for index,num in enumerate(nums):
            value=target-num
            if value in lookup_dict:
                return [lookup_dict[value],index]
            lookup_dict[num]=index

