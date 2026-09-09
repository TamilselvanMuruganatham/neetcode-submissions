class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_values=dict()
        
        for string in strs:
            chars=[0]*26
            for char in string:
                chars[ord(char)-ord('a')]+=1
            chars=tuple(chars)
            if chars not in key_values:
                key_values[chars]=[string]
            else:
                key_values[chars].append(string)
        return list(key_values.values())


        
