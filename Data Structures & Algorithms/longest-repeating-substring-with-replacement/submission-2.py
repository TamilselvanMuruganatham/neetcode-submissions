class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=0
        count={}
        max_freq=result=0
        for end in range(len(s)):
            char=s[end]
            count[char]=count.get(char,0)+1
            max_freq=max(count[char],max_freq)
            while (end-start+1) - max_freq>k:
                count[s[start]] -= 1
                start+=1
            result=max(result,end-start+1)
        return result


       
            


        
        