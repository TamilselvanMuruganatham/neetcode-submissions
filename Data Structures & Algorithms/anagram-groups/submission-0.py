class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=dict()
        for string in strs:
            key=tuple(sorted(string))
            if key not in hash_map:
                hash_map[key]=[string]
            else:
                hash_map[key].append(string)
            
            
        return list(hash_map.values())