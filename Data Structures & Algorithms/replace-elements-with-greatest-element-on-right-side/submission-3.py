class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        great=arr[-1]
        for _ in range(len(arr)-1,-1,-1):
            value=arr[_]
            arr[_]=great
            great=max(great,value)
        arr[-1]=-1
        return arr
