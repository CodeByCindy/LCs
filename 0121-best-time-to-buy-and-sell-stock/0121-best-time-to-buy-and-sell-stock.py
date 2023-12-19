class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
        # res = 0 
        # l, r = 0, 1
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         res = max(res, prices[r]-prices[l])
        #     else:
        #         l = r
        #     r += 1
        # return res