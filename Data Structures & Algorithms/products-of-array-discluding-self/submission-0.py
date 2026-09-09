from functools import reduce
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans=[]
        for index,value in enumerate(nums):
            ans.append(
                reduce(lambda a,b:a*b,nums[:index]+nums[index+1:])
            )
                
        return ans

            

