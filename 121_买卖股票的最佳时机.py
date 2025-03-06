class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)

        if m < 2:
            return 0

        m = 1
        n = 0
        min_val = prices[0]
        profit = 0

        while m < len(prices):
            min_val = min(min_val, prices[m-1])
            n = prices[m] - min_val
            if profit < n:
                profit = n
            m += 1
        return profit
        