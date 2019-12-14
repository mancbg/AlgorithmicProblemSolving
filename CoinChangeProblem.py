# def getWays(total, coins):
def coin_change_problem(total, coins):
    ways = 0

    if len(coins) != 0 or total != 0:
        # coins = sorted(coins)

        # DP
        coin_dp = [1] + [0] * total

        for coin in coins:
            for i in range(coin, total + 1):
                coin_dp[i] += coin_dp[i - coin]

        return coin_dp[total]

    return ways


def main():
    total, types = map(int, input().split())
    coins = list(map(int, input().split()))

    assert types == len(coins)

    print(coin_change_problem(total, coins))


if __name__ == '__main__':
    main()
