class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_count=0
        hash_map={}
        start=end=0
        while end<len(s):
            char=s[end]
            hash_map[char]=hash_map.get(char,0)+1

            while hash_map and hash_map[char]>1:
                hash_map[s[start]] -= 1
                start+=1
            
            long_count=max(long_count,(end-start+1))
            end+=1

        return long_count

            
            
                

        


                

