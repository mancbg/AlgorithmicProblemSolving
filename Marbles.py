import operator as op
from functools import reduce


def marbles(nums, colors):
    return n_combinations_k(nums - 1, colors - 1)


def n_combinations_k(n, k):
    k = min(k, n - k)
    return int(reduce(op.mul, range(n, n - k, -1), 1) / reduce(op.mul, range(1, k + 1), 1))


def main():

    for _ in range(int(input())):
        n, k = map(int, input().split())
        print(marbles(n, k))


if __name__ == '__main__':
    main()
