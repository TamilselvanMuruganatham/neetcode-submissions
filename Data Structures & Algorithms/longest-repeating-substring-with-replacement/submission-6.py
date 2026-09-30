class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=end=0
        char_map={}
        result=max_freq=0
        
        while end<len(s):
            char=s[end]
            char_map[char]=char_map.get(char,0)+1

            while ((end-start+1) - max(char_map.values()))>k:
                char_map[ s[start] ]-=1
                start += 1
            max_freq = max(max_freq, end-start+1)
            end+=1    

        return max_freq
    


       
            


        
        