from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        c1=Counter(s)
        c2=Counter(t)
        return all( c1[key]==c2.get(key,0)  for key in c1)

        