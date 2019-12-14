import math


def number_of_factors(n):
    factors = dict()
    result = 1
    for num in n:
        size = int(math.sqrt(num)) + 1
        i = 2
        while i <= size:
            count = 0
            while num % i == 0:
                count += 1
                num = num // i
            if count > 0:
                if i not in factors:
                    factors[i] = 1
                factors[i] = factors.get(i) + count
            if i == 2:
                i += 1
            else:
                i += 2
        if num != 1:
            if num not in factors:
                factors[num] = 1
            factors[num] = factors.get(num) + 1
    for i in factors.keys():
        result *= factors[i]
    return result


def main():
    T = int(input())

    for T_itr in range(T):
        input()
        n = list(map(int, input().strip().split()))

        result = number_of_factors(n)
        print(result)


if __name__ == '__main__':
    main()
