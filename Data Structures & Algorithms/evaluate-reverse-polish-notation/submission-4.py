class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        if len(tokens)==1:
            return int(tokens[0])
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                value_a,value_b=stack[-2:]
                stack=stack[:-2]
                match token:
                    case '+':
                        ans=value_a+value_b
                    case '-':
                        ans=value_a-value_b
                    case '*':
                        ans=value_a*value_b
                    case '/':
                        ans=value_a/value_b
                stack.append(int(ans))
        return int(ans)




