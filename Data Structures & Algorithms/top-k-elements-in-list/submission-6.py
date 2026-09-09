import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1
        arr=[]
        for key,value in hash_map.items():
            heapq.heappush(arr,(value,key))

            if len(arr)>k:
                heapq.heappop(arr)
        return [x[-1] for x in arr]

        
        
        