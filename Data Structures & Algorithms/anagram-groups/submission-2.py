class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_values=dict()
        for string in strs:
            hashed=tuple(sorted(string))
            if hashed not in key_values:
                key_values[hashed]=[string]
            else:
                key_values[hashed].append(string)
        return list(key_values.values())
