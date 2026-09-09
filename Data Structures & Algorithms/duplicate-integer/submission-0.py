class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookUp=set()
        for num in nums:
            if num in lookUp:
                return True
            lookUp.add(num)
        return False
        