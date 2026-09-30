class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_count=0
        hash_map={}
        start=end=0
        while end<len(s):
            char=s[end]
            if char in hash_map and hash_map[char]>=start:
                start=hash_map[char]+1
            
            hash_map[char]=end
            long_count=max(long_count,(end-start+1))
            end+=1

        return long_count

            
            
                

        


                

