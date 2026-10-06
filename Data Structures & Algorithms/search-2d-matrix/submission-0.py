class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            if array[0]<= target <= array[-1]:
                array_set=set(array)
                return target in array
        return False