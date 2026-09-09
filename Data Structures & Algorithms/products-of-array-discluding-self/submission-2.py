class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nod_arr=[1]*len(nums)
        prod=1
        for index,value in enumerate(nums):
            nod_arr[index]=prod
            prod *= value
        prod=1
        while index>=0:
            nod_arr[index] *= prod
            prod *= nums[index]
            index -= 1
        return nod_arr