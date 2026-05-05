class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                diff = prices[j] - prices[i]
                maxi = max(diff,maxi)
        
        return maxi