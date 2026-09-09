class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=0
        count={}
        result=max_freq=0
        
        for end,char in enumerate(s):
            count[char] =  count.get(char,0)+1
            max_freq=max(max_freq,count[char])

            while(end - start + 1)-max_freq>k:
                count[s[start]]-=1
                start+=1
            result=max(end-start+1,result)
        return result 
    


       
            


        
        