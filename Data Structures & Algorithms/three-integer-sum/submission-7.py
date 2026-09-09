class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        targets=[]
        nums.sort()
        for index , num in enumerate(nums[:-2]):
            if index>0 and nums[index]==nums[index-1]:continue
            start=index+1
            end=len(nums)-1

            while start<end:
                total=num+ nums[start]+nums[end]
                if total == 0:
                    targets.append([num,nums[start],nums[end]])
                    
                    start+=1
                    end-=1
                    
                    
                    while start<end and nums[start] == nums[start-1]:
                        start+=1
                    
                    while start<end and nums[end]== nums[end+1]:
                        end-=1

                elif total<0:
                    start+=1
                else:
                    end-=1

        return targets