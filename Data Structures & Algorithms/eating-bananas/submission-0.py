import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles=max(piles)
        left=1
        right=max_piles
        min_eat=float('inf')
        while left<=right:
            mid=(left+right)//2
            hours=sum(math.ceil(pile/mid) for pile in  piles )
            if hours<=h:
                right=mid-1
                min_eat=min(min_eat,mid)
            else:
                left=mid+1
        return min_eat


        