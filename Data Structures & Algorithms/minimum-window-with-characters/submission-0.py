from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        hash_map=Counter(t)
        sub_map={}
        start=end=0
        min_len=float('inf')
        result=''
        while end<len(s):
            char=s[end]
            if char in hash_map:
                sub_map[char]=sub_map.get(char,0)+1

            end+=1

            while (start<end) and (
                s[start] not in hash_map or
                sub_map.get(s[start],0)>hash_map.get(s[start],0)
            ):
                if s[start] in sub_map:
                    sub_map[s[start]] -= 1
                
                start+=1
            if all( sub_map.get(key,0)>=hash_map[key]  for key in hash_map):    
                if end-start<min_len:
                    result=s[start:end]
                    min_len=end-start
        return result
            

        