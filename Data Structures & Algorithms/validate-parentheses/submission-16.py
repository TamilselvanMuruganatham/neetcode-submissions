class Solution:
    def isValid(self, s: str) -> bool:
        hash={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        temp=''
        for x in s:
            if temp and  x in hash and temp[-1]==hash[x]:
                temp=temp[:-1] 
            else:
                temp+=x
        return not temp