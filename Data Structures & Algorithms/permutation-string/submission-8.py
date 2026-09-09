from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map=dict(Counter(s1))
        sub_map={}
        start=end=0
        result=''
        while end<len(s2):
            char=s2[end]
            if char in hash_map:
                sub_map[char]=sub_map.get(char,0)+1
                end+=1
            else:
                end+=1
                start=end
                sub_map={}
                continue
            while any(sub_map.get(key,0)>hash_map[key] for key in hash_map):
                if s2[start] in sub_map:
                    sub_map[s2[start]]-=1
                start+=1
                
            if all( sub_map.get(key,0)==hash_map[key] for key in hash_map):
                return True
            
            
        return all( sub_map.get(key,0)==hash_map[key] for key in hash_map)

                      
