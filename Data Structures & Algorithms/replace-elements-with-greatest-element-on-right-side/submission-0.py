class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        great=arr[-1]
        for i in range(len(arr)-1,-1,-1):
            value=arr[i]
            arr[i]=great
            great=max(great,value)
        arr[-1]=-1
        return arr
