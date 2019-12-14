def array_transform(n, k, numbers):
    if n <= 2:
        return "YES"

    mods = dict()

    for i in range(n):
        mod = numbers[i] % (k + 1)
        if mod in mods:
            mods[mod] = mods.get(mod) + 1
        elif len(mods) < 2:
            mods[mod] = 1
        else:
            return "NO"

    return "YES" if max(list(mods.values())) >= n - 1 else "NO"


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        array = list(map(int, input().split()))

        assert n == len(array)

        print(array_transform(n, k, array))


if __name__ == '__main__':
    main()
