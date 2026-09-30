from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        if s==t:
            return t
        targetCount=Counter(t)
        need=len(targetCount)
        have=start=0
        subCount={}
        subString=''
        minWindow=float('inf')
        for end in range(len(s)):
            char = s[end]
            if char in targetCount:
                subCount[char]=subCount.get(char,0)+1
                if subCount[char]==targetCount[char]:
                    have += 1
            while have==need:
                windowSize=end-start+1
                if windowSize<minWindow:
                    minWindow=windowSize
                    subString=s[start:end+1]
                leftChar=s[start]
                if leftChar in targetCount:
                    subCount[leftChar] -= 1
                    if subCount[leftChar]<targetCount[leftChar]:
                        have -= 1
                start+=1
        return subString
        
