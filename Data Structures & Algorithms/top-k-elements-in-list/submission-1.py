class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1
        most_frequents=sorted(hash_map.keys() ,key=lambda x: hash_map[x],reverse=True)
        return most_frequents[:k]