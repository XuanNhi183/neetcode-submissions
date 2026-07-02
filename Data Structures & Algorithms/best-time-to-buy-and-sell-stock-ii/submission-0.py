class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i in range (len(prices)-1):
            if prices[i] < prices[i+1]:
                prof = prices[i+1] - prices[i]
                maxProf+=prof
        return maxProf
        