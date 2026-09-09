class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        targets=[]
        nums=sorted(nums)
        array_len=len(nums)
        for index in range(len(nums[:-2])):
            if index > 0 and nums[index-1]==nums[index]:
                continue
            start=index+1
            end=array_len-1
            while start<end:
                value =  nums[index] + nums[start] + nums[end]
                if value == 0:
                    targets.append([nums[index] , nums[start] , nums[end]])
                    start+=1
                    end-=1

                    while start<end and nums[end] == nums[end+1]:
                        end-=1
                    while start<end and nums[start] == nums[start-1]:
                        start+=1
                    
                if value>0 :
                    end-=1

                if value<0:
                    start+=1
                    

        return targets