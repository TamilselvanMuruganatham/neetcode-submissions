class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map={}
        for index, number in enumerate(numbers):
            req=target-number
            if req in hash_map:
                return [hash_map[req]+1,index+1]
            hash_map[number]=index
        return []