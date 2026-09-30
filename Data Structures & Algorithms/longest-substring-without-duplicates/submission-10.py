class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_count=sub_count=0
        hash_map=set()
        start=end=0
        while end<len(s):
            if s[end] in hash_map:
                long_count=max(long_count,sub_count)
                while s[end] in hash_map:
                    hash_map.remove(s[start])
                    start+=1
                    sub_count-=1
            else:
                hash_map.add(s[end])
                sub_count+=1
                end+=1

        long_count=max(long_count,sub_count)

        return long_count

            
            
                

        


                

