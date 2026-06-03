class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles): return max(piles)

        l, r = 1, max(piles)
        valid = r

        while l <= r:
            m = (l+r)//2
            count = 0

            for num in piles:
                count += math.ceil(num/m)
  
            if count <= h: 
                valid = min(valid,m)
                r = m - 1
            else:
                l = m + 1
        return valid



