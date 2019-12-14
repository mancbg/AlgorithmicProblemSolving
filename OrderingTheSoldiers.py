# cook your dish here
def orderingTheSoldiers(n, soldiers):
    result = [-1] * n
    ranks = [x for x in range(1, n + 1)]
    for index in range(n - 1, -1, -1):
        result[index] = ranks.pop(index - soldiers[index])
    print(*result)


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        soldiers = list(map(int, input().split()))

        assert n == len(soldiers)
        orderingTheSoldiers(n, soldiers)


if __name__ == '__main__':
    main()
