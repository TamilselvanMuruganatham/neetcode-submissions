from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=defaultdict(list)
        
        for string in strs:
            char_index=[0]*26
            for char in string:
                index=ord(char)-ord('a')
                char_index[index]+=1
            hash_map[tuple(char_index)].append(string)
            

            
            
        return list(hash_map.values())