class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len=len(nums)
        nod_arr=[1]*arr_len
        prod=1
        for index in range(arr_len):
            nod_arr[index]=prod
            prod *= nums[index]
        prod=1
        for index in range(arr_len-1,-1,-1):
            nod_arr[index] *= prod
            prod *= nums[index]
        return nod_arr