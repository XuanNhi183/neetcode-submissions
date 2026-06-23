class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf=0
        min_price=prices[0]
        for price in prices:
            min_price=min(min_price,price)
            profit=price-min_price
            maxProf=max(maxProf,profit)
        return maxProf

