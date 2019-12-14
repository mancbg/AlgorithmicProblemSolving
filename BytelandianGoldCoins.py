COIN_EXCHANGE = dict()


def byteland_gold_coins(n):
    if n == 0:
        return n
    elif n not in COIN_EXCHANGE:
        COIN_EXCHANGE[n] = max(n,
                               byteland_gold_coins(n // 2) + byteland_gold_coins(n // 3) + byteland_gold_coins(n // 4))

    return COIN_EXCHANGE[n]


def main():
    while True:
        try:
            coin = int(input())
            dollars = byteland_gold_coins(coin)
            print(dollars)
        except:
            break


if __name__ == '__main__':
    main()
