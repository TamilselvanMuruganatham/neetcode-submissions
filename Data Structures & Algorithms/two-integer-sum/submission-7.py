class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for index, value in enumerate(nums):
            summ=target-value
            if summ in hash_map:
                return [hash_map[summ]  ,index]
            else:
                hash_map[value]=index