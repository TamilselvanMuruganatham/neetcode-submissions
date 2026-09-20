class Solution:
    def isValid(self, s: str) -> bool:
        hash={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        temp=[]
        for x in s:
            if temp and x in hash and temp[-1]==hash[x]:
                temp.pop()
            else:
                temp.append(x)
        return not temp