class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dict1,dict2={},{}
        for str1,str2 in zip(s,t):
            dict1[str1]=dict1.get(str1,0)+1
            dict2[str2]=dict2.get(str2,0)+1
        values=( dict1[key]==dict2.get(key,'') for key in dict1  )
        return all(values)

