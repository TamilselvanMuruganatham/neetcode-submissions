class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=end=0
        char_map={}
        result=max_freq=0

        while end<len(s):
            c = s[end]
            
            char_map[c]=char_map.get(c,0)+1
            
            max_freq=max(max_freq,char_map[c])
            while (end-start+1) - max_freq >k:
                char_map[s[start]]-=1
                start+=1
                # max_freq=max(max_freq,char_map[s[start]])
            result=max(result, end-start+1)
            end+=1

        

        return result
    


       
            


        
        