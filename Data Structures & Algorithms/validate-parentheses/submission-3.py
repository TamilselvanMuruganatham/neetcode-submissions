class Solution:
    def isValid(self, s: str) -> bool:
        key_map={
            '}':'{',
            ')':'(',
            ']':'['
            }
        stack=[]
        for char in s:
            if char not in key_map:
                stack.append(char)
            else:
                if stack and stack[-1] == key_map[char]:
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack) == 0 
        
                