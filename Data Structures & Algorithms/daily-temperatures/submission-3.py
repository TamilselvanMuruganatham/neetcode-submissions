class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        distance=[0]*len(temperatures)
        end=len(temperatures)-1

        while end>=0:
          
            value=temperatures[end]
            while stack and value >= temperatures[ stack[-1] ]:
                stack.pop()
            dist=stack[-1]-end if stack else 0
            distance[end]=dist

            stack.append(end)
            end -= 1
        return distance



                
