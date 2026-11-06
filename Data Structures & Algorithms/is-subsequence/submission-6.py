class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        t_index=s_index=0
        counter=0  
        while t_index<len(t) and s_index<len(s):
            if t[t_index]==s[s_index]:
                counter += 1
                s_index+=1
            t_index+=1
        
        return len(s)==counter