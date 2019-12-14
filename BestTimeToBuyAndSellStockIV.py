class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        days = len(prices)

        if k <= 0 or days <= 1:
            return 0

        if k > days / 2:
            profit = 0

            for i in range(1, days):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        dp = [0 * days] * (k + 1)

        for i in range(1, k + 1):
            max_profit = dp[i - 1][0] - prices[0]
            for j in range(1, days):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_profit)
                max_profit = max(max_profit, dp[i - 1][j] - prices[j])

        return dp[k][days - 1]


def main():
    prices = list(map(int, input().strip().split()))
    k = int(input())
    Solution().maxProfit(k, prices)


if __name__ == '__main__':
    main()
