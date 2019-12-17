import math


class Solution:
    def maxProfit(self, k, prices):
        days = len(prices)

        if days <= 1 or k < 1:
            return 0

        if k >= days // 2:
            profit = 0

            for i in range(1, days):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        k = min(k, days // 2)
        dp = []
        for i in range(k + 1):
            lst = []
            for j in range(days):
                lst.append(0)
            dp.append(lst)

        for i in range(1, k + 1):
            max_profit = -math.inf
            for j in range(1, days):
                max_profit = max(max_profit, dp[i - 1][j - 1] - prices[j - 1])
                dp[i][j] = max(dp[i][j - 1], max_profit + prices[j])

        return dp[k][days - 1]